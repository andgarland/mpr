from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #regex below could easily be wrong/not what we want
    url(r'^courses/(?P<course_num>.+)/$', views.course, name = 'course'),
    #url(r'^login/$', auth_views.login, name = 'login'),
]