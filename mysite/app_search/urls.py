from django.contrib import admin
from django.urls import path,include
from .views import  SearchResultsView
from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', views.Home, name='home'),
    path('app_details/<int:id>', views.App_details, name='app_details'),
    path('google/', views.Google, name='google'),

]