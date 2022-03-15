from django.urls import path
from library_app import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('success/', views.success_page, name='success_page'),
    path('library/', views.library_page, name='library_page'),
    path('chart/', views.chart_page, name='chart_page'),
]
