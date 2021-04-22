from django import forms
from django.forms import fields
#创建user的表单 包括用户账户（电话） 和用户密码
class UserForm(forms.Form):
    username = forms.CharField(label="用户账户",max_length=128)
    password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    isAdminUnit = (('doctor', u'医生'), ('pacient', u'就诊人'),)
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    age = forms.CharField(label='年龄',max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label=u'电话', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dete_id = forms.CharField(label=u'编号', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    isAdmin = forms.ChoiceField(label=u'身份', choices=isAdminUnit)
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class uploadForm(forms.Form):
    doctorName = fields.CharField(label="医生姓名",max_length=128)
    dcmImage = fields.FileField()
