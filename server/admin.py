from django.contrib import admin
from server.models import User
class PacientAdmin(admin.ModelAdmin):
    list_display = ['name','sex','age','telephone','dete_id','id_card','password','isAdmin','time']
admin.site.register(User,PacientAdmin)

# Register your models here.
