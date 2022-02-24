from django.urls import path
from library_app import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('success/', views.success_page, name='success_page'),
]
