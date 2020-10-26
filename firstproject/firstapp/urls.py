from django.conf.urls import url
from firstapp import views

app_name='firstapp'

urlpatterns=[
  url(r'^$',views.index,name='index'),
  url(r'^admin/',views.admin,name='admin'),
  url(r'^help/',views.help,name='help'),
  url(r'^mylogin/',views.mylogin,name='mylogin'),
  url(r'^registration/',views.register,name='registration'),
  url(r'^relative/',views.relative,name='relative'),
  url(r'^logout/$',views.user_logout,name='logout'),
  url(r'^login/',views.user_login,name='user_login')



]