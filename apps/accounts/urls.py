from django.urls import path

from apps.accounts import views


# Create your urls here.

urlpatterns = [
    path('', views.CustomUserAPIView.as_view()),
    path('<int:pk>/', views.CustomUserRetrieveAPIView.as_view()),

    path('register/', views.RegisterAPIView.as_view()),

    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),

    path('change_password/<int:pk>/', views.ChangePasswordAPIView.as_view()),
]
