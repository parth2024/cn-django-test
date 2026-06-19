from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oom/', views.trigger_oom, name='trigger_oom'),
]