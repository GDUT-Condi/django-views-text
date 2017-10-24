from django.conf.urls import  url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^(?P<a1>\d+)/(?P<a2>\d+)/(?P<a3>\d+)/$', views.detail,name='detil'),

    url(r'^getText1/$', views.getText1),
    url(r'^getText2/$', views.getText2),
    url(r'^getText3/$', views.getText3),

    url(r'^postText1/$', views.postText1),
    url(r'^postText2/$', views.postText2),

    url(r'^cookieText/$', views.cookieText),

    url(r'^redText1/$', views.redText1),
    url(r'^redText2/$', views.redText2),

    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3),
]
