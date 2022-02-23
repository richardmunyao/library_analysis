from django.urls import path
from library_app import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]
