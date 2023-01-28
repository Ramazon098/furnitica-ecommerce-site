from apps.accounts.views.user import (
    CustomUserAPIView,
    CustomUserRetrieveAPIView,
    EditProfileAPIView,
)

from apps.accounts.views.auth import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
)

from apps.accounts.views.password import (
    ChangePasswordAPIView,
    SendCodeAPIView,
    VerifyOtpAPIView,
    ResetPasswordAPIView,
)


__all__ = [
    "CustomUserAPIView",
    "CustomUserRetrieveAPIView",
    "EditProfileAPIView",
    "RegisterAPIView",
    "LoginAPIView",
    "LogoutAPIView",
    "ChangePasswordAPIView",
    "SendCodeAPIView",
    "VerifyOtpAPIView",
    "ResetPasswordAPIView",
]
