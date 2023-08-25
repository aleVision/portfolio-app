from django.urls import path
from cv_projects import views

urlpatterns = [
    path('', views.all_projects),    
]