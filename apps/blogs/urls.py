from django.urls import path
from apps.blogs import views


# Create your urls here.

urlpatterns = [
    path('', views.BlogPostAPIView.as_view()),
    path('<int:pk>/', views.BlogDetailAPIView.as_view()),
    path('comments/', views.CommentAPIView.as_view()),
    path('comment/<int:pk>/', views.CommentDetailAPIView.as_view()),
]
