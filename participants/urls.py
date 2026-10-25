from django.urls import path
from . import views

urlpatterns = [
    path('', views.participants_list, name='participants_list'),
    path('<str:part_id>/', views.participant_detail, name='participant_detail'),
]