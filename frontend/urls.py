from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name="summary"),
    path('about', views.about, name="about"),
]