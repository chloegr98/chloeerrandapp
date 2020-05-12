from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name="api"),
    path('errand-summary/', views.errandSummary, name="errand-summary"),
    path('errand-info/<str:pk>/', views.errandInfo, name="errand-info"),
    path('errand-create/', views.errandCreate, name="errand-create"),
    path('errand-update/<str:pk>/', views.errandUpdate, name="errand-update"),
    path('errand-delete/<str:pk>/', views.errandDelete, name="errand-delete"),
]

