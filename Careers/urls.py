from django.urls import path
from . import views

urlpatterns = [
    # ✅ Get all careers
    path('', views.get_all_careers, name='career-list'),

    # ✅ Get details of a specific career
    path('<int:pk>/', views.get_career_detail, name='career-detail'),

    # ✅ Apply for a specific career
    path('<int:pk>/apply/', views.apply_for_career, name='career-apply'),
]
