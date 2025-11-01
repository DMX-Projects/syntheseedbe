from django.urls import path
from . import views

urlpatterns = [
    # GET → Fetch all career listings | POST → Add new career (optional)
    path('', views.get_all_careers, name='career-list'),

    # GET → Fetch a single career by its ID (for “View Role” page)
    path('<int:id>/', views.get_career_detail, name='career-detail'),
]