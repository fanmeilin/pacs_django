from django.contrib import admin
from server.models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','sex','age','telephone','dete_id','password','isAdmin']
admin.site.register(User,UserAdmin) #后台管理

# Register your models here.
