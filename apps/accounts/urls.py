from django.urls import path

from apps.accounts import views


# Create your urls here.

urlpatterns = [
    path('', views.CustomUserAPIView.as_view()),
    path('<int:pk>/', views.CustomUserRetrieveAPIView.as_view()),
]
