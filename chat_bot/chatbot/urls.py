from django.urls import path,re_path
from django.urls import include, re_path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('search/', views.search, name='search'),
    # re_path(r'^search/$', views.search),
    # re_path(r'^search/(?P<text>\w{0,50})/$', views.profile_page,),
]