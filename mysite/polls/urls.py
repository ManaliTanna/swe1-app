from django.urls import path

from . import views
"""
path()
route - urlpattern string
view - on finding matching urlpattern, django will call this specified view pattern with HttpRequest as arg
kwargs - arbitrary arguments
name - to refer to this url from anywhere
"""
urlpatterns = [
    path('', views.index, name='index'),
]