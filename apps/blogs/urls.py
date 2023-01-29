from django.urls import path
from apps.blogs import views


# Create your urls here.

urlpatterns = [
    path('', views.BlogPostAPIView.as_view()),
    path('<int:pk>/', views.BlogPostAPIView.as_view())
]
