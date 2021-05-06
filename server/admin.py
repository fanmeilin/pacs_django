from django.contrib import admin
from server.models import User,Doctor
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','sex','age','telephone','dete_id','password','isAdmin']
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["dete_id","Dname","Dtelephone","Pname","Ptelephone","Psex","Page","Pimgsrc","Pmodelresult","Pdoctorresult","advise"]
admin.site.register(User,UserAdmin) #后台管理
admin.site.register(Doctor,DoctorAdmin)
# Register your models here.
