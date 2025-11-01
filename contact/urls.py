from django.urls import path
from .views import submit_contact_form, login_view  # 👈 Make sure this import exists

urlpatterns = [
    path('submit/', submit_contact_form, name='submit_contact'),
    path('login/', login_view, name='login'),  # 👈 Added login endpoint
]
