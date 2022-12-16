from django.urls import path, include


# Create your urls here.

urlpatterns = [
    path('users/', include('apps.accounts.urls')),
]
