from django.shortcuts import render,redirect,HttpResponse
from django.http import FileResponse
from server.models import User,Doctor
from .forms  import UserForm
from .forms  import RegisterForm
from django.http import JsonResponse
from .forms  import uploadForm
from image_detect.function import predictImgset,readModel
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
import uuid
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
#登录页面表单处理
def logout(request):
    if not request.session.get('is_login',None): #未登录就直接跳转到index
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")
def login(request):
    if(request.session.get('is_login',None)): #不允许重复登录
        return redirect('/index/')
    message = ""
    if(request.method=="POST"):
        login_form = UserForm(request.POST)
        if(login_form.is_valid()):
            username = login_form.cleaned_data['username'] #在字典中获取具体值
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(telephone=username)
                # pacient = Doctor.objects.filter(Dtelephone = username)
                if user.password==password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.telephone
                    request.session['user_name'] = user.name
                    request.session['isAdmin'] = user.isAdmin
                    request.session['dete_id'] = user.dete_id
                    return redirect('/index/')
                else:
                    message = "密码不正确"
            except:
                message = "用户不存在！"
        return render(request,'login.html',locals()) #内置函数
    login_form = UserForm()
    return render(request,'login.html',locals())
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            age = register_form.cleaned_data['age']
            sex = register_form.cleaned_data['sex']
            telephone = register_form.cleaned_data['telephone']
            dete_id = register_form.cleaned_data['dete_id']
            isAdmin = register_form.cleaned_data['isAdmin']
            # list_display = ['name', 'sex', 'age', 'telephone', 'dete_id', 'password', 'isAdmin']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(telephone=telephone)
                if same_name_user:  # 用户名唯一
                    message = '该手机账户已被注册，请使用别的号码！'
                    return render(request, 'register.html', locals())
        # 当一切都OK的情况下，创建新用户
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.age = age
                new_user.telephone = telephone
                new_user.dete_id = dete_id
                new_user.isAdmin = isAdmin
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())
def upload(request):
    if (not (request.session.get('is_login', None)and (request.session.get('isAdmin', None)=='pacient'))):
        # 登录状态不允许注册。你可以修改这条原则！
        message = "请以就诊人身份先登录"
        return render(request, 'login.html', {'message': message})  # 内置函数
    if(request.method=='GET'):
        return render(request,'upload.html',locals())
    if request.method=="POST":
        dcmImage = request.FILES.get("dcmImage", None)
        print("是否已经预约过",dcmImage)
        doctorName = request.POST.get('doctorName')
        doctorid = request.POST.get('doctorid')
        try:
            print("进行查找",doctorid)
            doctor = User.objects.get(dete_id=doctorid)
            userzh = request.session['user_id']
            print(userzh)
            print("doctor object:", doctor)
            pacient = User.objects.get(telephone = userzh )
            print("pacient object",pacient)
            if not(doctor.name==doctorName):
                message = "请核实医生的姓名以及对应编号！"
            if (dcmImage):
                # "dete_id","Dname", "Dtelephone", "Pname", "Ptelephone", "Pimgsrc", "Pmodelresult", "Pdoctorresult", "advise"
                # 当一切都OK的情况下，创建医患对应信息
                if not(request.session.get('upload_img', None)): #如果尚未提交
                    position = os.path.join(".\static\imageUnit", dcmImage.name)
                    print("position",position)
                    f = open(position, 'wb+')
                    for chunk in dcmImage.chunks():
                        f.write(chunk)
                    f.close()
                    #模型预测图像的诊断结果
                    model = readModel(r"./image_detect/model200.h5")
                    result = predictImgset(model, [position])
                    print("预测结果：",result)
                    # 保存数据库信息 就诊人id 预约医生 图片路径
                    dete_id = request.session['dete_id']
                    Dname = doctor.name
                    Dtelephone = doctor.telephone
                    Pname = request.session['user_name']
                    Ptelephone = request.session['user_id']
                    Psex = pacient.sex
                    Page = pacient.age
                    # Pimgsrc = "." + position  # 转换存储路径
                    Pimgsrc = os.path.join("\static\imageUnit", dcmImage.name) #静态文件的形式进行存储
                    request.session['upload_img'] = True
                    new_user = Doctor.objects.create()
                    new_user.dete_id = dete_id
                    new_user.Dname = Dname
                    new_user.Dtelephone = Dtelephone
                    new_user.Pname = Pname
                    new_user.Psex = Psex
                    new_user.Page = Page
                    new_user.Ptelephone = Ptelephone
                    new_user.Pimgsrc = Pimgsrc
                    new_user.Pmodelresult = result[0]
                    print("保存数据库")
                    new_user.save()
                    request.session['upload_img'] = True
                    return redirect('/index/')
                else:
                    message = "已经预约过了，不可重复预约！"
            else:
                message = "请核实医生的姓名以及对应编号！"
        except:
            message = "出错！"
        return render(request, 'upload.html', {'message': message})
    return render(request,'upload.html')
def index(request):
    people_info = User.objects.all()
    return render(request,'index.html',{'people_info':people_info})
def dcmTemp(request):
    return render(request,'dcmtemp.html')
@csrf_exempt
def ajex_detect_Dresult(request):
    Pdoctorresult = request.POST.get('Pdoctorresult')
    dete_id = request.POST.get('dete_id')
    # print("诊断结果:",Pdoctorresult)
    # print("id:",dete_id)
    message = "无"
    try:
        obj = Doctor.objects.get(dete_id=dete_id)
        obj.Pdoctorresult = Pdoctorresult
        obj.save()
        message = "诊断结果成功上传系统！"
    except:
        message="诊断结果上传出错！"
    print(message)
    return JsonResponse({'message': message})

@csrf_exempt
def ajex_detect_Dadvice(request):
    adviseResult = request.POST.get('adviseResult')
    dete_id = request.POST.get('dete_id')
    message = "无"
    try:
        obj = Doctor.objects.get(dete_id=dete_id)
        obj.advise = adviseResult
        obj.save()
        message = "诊断建议成功上传至系统！"
    except:
        message="诊断建议上传出错！"
    print(message)
    return JsonResponse({'message':message})

def dcmViewer(request):
    if (not (request.session.get('is_login', None)and (request.session.get('isAdmin', None)=='doctor'))):
        # 登录状态不允许注册。你可以修改这条原则！
        message = "请以医师身份先登录再访问dcm查看器！"
        return render(request, 'login.html', {'message':message})  # 内置函数
    # people_info = User.objects.all() #分页
    # 测试
    current_page = request.GET.get('p')
    print("获取当前目录", current_page)
    if not current_page:
        current_page=1
    current_page = int(current_page)
    print("获取当前目录(int)",current_page)
    userzh = request.session['user_id']
    diagnose_list = Doctor.objects.filter(Dtelephone=userzh)  # 查找对应账号的订单
    # print("查找订单", diagnose_list)
    paginator = Paginator(diagnose_list, 1)
    if (diagnose_list.count)==0:
        return HttpResponse("暂无病人")
    try:
        diagnose = paginator.page(current_page)
        # pacient = User.objects.get(telephone="15700000001") #筛选条件 就诊人的具体信息
        # dignosetable = Doctor.objects.get(Dtelephone="13700000001") #医生订单
    except PageNotAnInteger:
        diagnose = paginator.page(1)
    except EmptyPage:
        diagnose = paginator.page(paginator.num_pages)
    pacient = diagnose.object_list[0]
    # print("就诊人",pacient)
    return render(request,'dcmViewer.html',{'pacient':pacient,'diagnose':diagnose})
def read(request):
    # return HttpResponse("Hello World")
    src = request.GET.get('src')
    print("获取下载路径：",src)
    file = open(src, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    file_name = os.path.split(src)[-1]
    print("文件名:",file_name)
    response['Content-Disposition'] = 'attachment;filename={}'.format(file_name)
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin"
    return response
def read0(request):
    src = request.GET.get('src')
    file = open('./testdcm/ImageFileName0080.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="0.dcm"'
    # response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin"
    return response
def read1(request):
    # file = open('./testdcm/ImageFileName0081.dcm', 'rb')
    file = open('./testdcm/ImageFileName0081.dcm','rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return response
def read2(request):
    file = open('./testdcm/ImageFileName0082.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="2.dcm"'
    return response
def read3(request):
    file = open('./testdcm/ImageFileName0083.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="3.dcm"'
    return response
def read4(request):
    file = open('./testdcm/ImageFileName0084.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="4.dcm"'
    return response
def read5(request):
    file = open('./testdcm/ImageFileName0085.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="5.dcm"'
    return response
def read6(request):
    file = open('./testdcm/ImageFileName0086.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="6.dcm"'
    return response
def read7(request):
    file = open('./testdcm/ImageFileName0087.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="7.dcm"'
    return response
def read8(request):
    file = open('./testdcm/ImageFileName0088.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="8.dcm"'
    return response
def read9(request):
    file = open('./testdcm/ImageFileName0089.dcm', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="9.dcm"'
    return response






