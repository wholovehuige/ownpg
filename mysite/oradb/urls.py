from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^jsondata/$',views.getJSONData,name='jsondata'),
    url(r'^home/$',views.getAllDbData),
    url(r'to_db_edit',views.to_db_edit,name='to_db_edit'),
    url(r'to_db_home/(?P<id>[0-9]+)$',views.to_db_home,name='to_db_home'),
    url(r'^dbMessage/(?P<id>[0-9]+)$',views.db_page ,name='dbMessage'),
    url(r'^testConn/(?P<id>[0-9]+)$',views.test_oracle1_conn ,name='testConn'),
    url(r'^editDbMessage',views.edit_dbPage,name='editDbMessage')
]