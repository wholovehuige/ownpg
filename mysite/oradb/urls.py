from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^jsondata/$',views.getJSONData,name='jsondata'),
    url(r'^home/$',views.getAllDbData),
    url(r'^dbMessage/(?P<id>[0-9]+)$',views.db_page ,name='dbMessage'),
    url(r'^testConn/(?P<id>[0-9]+)$',views.test_oracle1_conn ,name='testConn'),
    url(r'^editDbMessage',views.edit_dbPage,name='editDbMessage')
]