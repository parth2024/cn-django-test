from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oom/', views.trigger_oom, name='trigger_oom'),
    path('segfault/', views.trigger_segfault, name='trigger_segfault'),
    path('db-crash/', views.trigger_db_crash, name='trigger_db_crash'),
    path('hang/', views.trigger_hang, name='trigger_hang'),
    path('disk-full/', views.trigger_disk_full, name='trigger_disk_full'),
]