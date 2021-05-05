from django.db import models

class User(models.Model):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    isAdminUnit = (('doctor',u'医生'),('pacient',u'就诊人'))
    name = models.CharField(u'姓名',max_length=128)
    sex = models.CharField(u"性别", max_length=32, choices=gender, default='男')
    age = models.CharField(u"年龄",max_length=128)
    telephone = models.CharField(u'电话',max_length=256,unique=True)
    dete_id = models.CharField(u'编号',max_length=128,unique=True)
    password = models.CharField(u'密码', max_length=256)
    isAdmin = models.CharField(u'身份',max_length=32,choices=isAdminUnit,default='就诊人')

    def __str__(self):
        return self.telephone

# Create your models here.
# 'name','sex','age','telephone','dete_id','id_card','password','isAdmin','time'
class Doctor(models.Model):
    dete_id = models.CharField(u'就诊编号', max_length=20, unique=True, default="")
    Dname = models.CharField(u'医生姓名',max_length=1282,default="")
    Dtelephone = models.CharField(u'医生电话',max_length=256,default="")
    Pname = models.CharField(u'就诊人姓名',max_length=20,default="")
    Ptelephone = models.CharField(u'就诊人电话', max_length=256,default="")
    Pimgsrc =  models.CharField(u'图像路径', max_length=256,default="")
    Pmodelresult = models.CharField(u'模型预测结果', max_length=256,default="无")
    Pdoctorresult = models.CharField(u'医生判断结果', max_length=256,default="")
    advise = models.CharField(u'医生建议', max_length=512,default="")
    def __str__(self):
        return self.dete_id

#"dete_id","Dname","Dtelephone","Pname","Ptelephone","Pimgsrc","Pmodelresult","Pdoctorresult","advise"