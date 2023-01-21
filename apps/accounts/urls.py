from django.urls import path

from apps.accounts import views


# Create your urls here.

urlpatterns = [
    path('', views.CustomUserAPIView.as_view()),
    path('<int:pk>/', views.CustomUserRetrieveAPIView.as_view()),

    path('register/', views.RegisterAPIView.as_view()),
    path('edit_profile/', views.EditProfileAPIView.as_view()),

    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),

    path('change_password/', views.ChangePasswordAPIView.as_view()),
    path('send_code/', views.SendCodeAPIView.as_view()),
    path('verify_otp/', views.VerifyOtpAPIView.as_view()),
    path('reset_password/', views.ResetPasswordAPIView.as_view(), name='reset_password'),
]
