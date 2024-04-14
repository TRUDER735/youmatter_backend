from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('admin/create/', views.create_admin, name='create_admin'),
    path('admin/<int:pk>/', views.admin_detail, name='admin_detail'),
    path('agent/create/', views.create_agent, name='create_agent'),
    path('agent/<int:pk>/', views.agent_detail, name='agent_detail'),
    path('client/create/', views.create_client, name='create_client'),
    
]
