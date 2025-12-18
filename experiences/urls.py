from django.urls import path

from . import views

app_name = 'experiences'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio_list, name='portfolio-list'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio-detail'),
    path('team/', views.team, name='team'),
    path('projects/YaldaCBC/HaafezFaal/', views.yalda_hafez_faal, name='yalda-haafez-faal'),
]
