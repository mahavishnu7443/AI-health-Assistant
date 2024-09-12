from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('add_reminder/', views.add_reminder, name='add_reminder'),
]
