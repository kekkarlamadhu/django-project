from django.urls import path
from . import views


app_name = 'myapp'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('special/', views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

]

