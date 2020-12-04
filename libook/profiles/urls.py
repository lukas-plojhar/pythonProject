from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='profile_detail'),
    # path('test/', views.TestView.as_view(), name='test_post'),
]