from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^managers/$', views.ManagerListView.as_view(), name='managers'),
    re_path(r'^manager/(?P<pk>\d+)$', views.ManagerDetailView.as_view(), name='manager-detail'),
]
