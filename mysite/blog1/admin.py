from django.contrib import admin
from .models import Article
# Register your models here.
#配置类
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','pub_time')
#注册
admin.site.register(Article,ArticleAdmin)