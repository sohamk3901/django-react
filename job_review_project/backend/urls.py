from django.urls import path
from . import views

urlpatterns = [
    path('', views.backendOverview, name='backend-overview'),
    path('candidate-list/', views.CandidateList, name='candidate-list'),
    path('candidate-detail/<str:pk>/', views.CandidateDetail, name='candidate-detail'),
    path('candidate-create', views.CandidateCreate, name='candidate-create'),
    path('candidate-update/<str:pk>/', views.CandidateUpdate, name='candidate-update'),
    path('candidate-delete/<str:pk>/', views.CandidateDelete, name='candidate-delete'),
]