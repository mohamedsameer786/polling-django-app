from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('votes/<str:pk>/', views.votes, name="votes"),
    path('votes/<str:pk>/results', views.results, name="results")
]