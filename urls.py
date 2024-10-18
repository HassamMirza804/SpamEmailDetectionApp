# mlapp/urls.py

from django.urls import path
from . import views  # Ensure this line is present

urlpatterns = [
    path('', views.home, name='home'),  # This should match the defined view
    path('check-spam/', views.SomeView.as_view(), name='some_view'),  # Add your other views here
]