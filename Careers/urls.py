from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_careers, name='career-list'),

    path('<int:pk>/', views.get_career_detail, name='career-detail'),
]