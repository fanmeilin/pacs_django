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
    dete_id = models.CharField(u'编号',max_length=128)
    password = models.CharField(u'密码', max_length=256)
    isAdmin = models.CharField(u'身份',max_length=32,choices=isAdminUnit,default='就诊人')

    def __str__(self):
        return self.telephone

# Create your models here.
# 'name','sex','age','telephone','dete_id','id_card','password','isAdmin','time'
class Doctor(models.Model):
    gender = (
        ('male','男'),('femalie','女')
    )
    name = models.CharField(u'姓名',max_length=20)
    password = models.CharField(u'密码',max_length=128)
    sex =  models.CharField(u"性别",max_length = 32,choices = gender,default='男')
    time = models.DateTimeField()