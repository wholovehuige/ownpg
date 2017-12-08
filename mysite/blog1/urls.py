from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^article/save/$',views.article_save,name="article_save"),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name="edit_page"),
    url(r'^edit/action/$',views.edit_action,name="edit_action"),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page')
]