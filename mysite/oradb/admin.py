from django.contrib import admin
from .models import dbMessage
# Register your models here.
#配置类
class dbMessageAdmin(admin.ModelAdmin):
    list_display = ('id','ip_address','port')
    # list_filter = ('pub_time',)
#注册
admin.site.register(dbMessage,dbMessageAdmin)