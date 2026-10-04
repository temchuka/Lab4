from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    re_path(r'^lease/(?P<lease_id>\d+)$', views.get_lease, name='get_lease'),
]
