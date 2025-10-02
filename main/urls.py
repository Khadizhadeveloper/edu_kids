from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers, name='teachers'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('api/courses/', views.api_courses, name='api_courses'),
]