from apps.blogs.views.blog import (
    BlogPostAPIView,
    BlogDetailAPIView,
)

from apps.blogs.views.comment import (
    CommentAPIView,
    CommentDetailAPIView,
)


__all__ = [
    "BlogPostAPIView",
    "BlogDetailAPIView",
    "CommentAPIView",
    "CommentDetailAPIView",
]
