from django.urls import path

from . import views

app_name = 'experiences'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio-detail'),
]
