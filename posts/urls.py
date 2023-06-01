from django.urls import path, include
from . import views

from .views import (
    CategorieListView,
    CategorieDetailView,
    CategorieEditView,
    CategorieDeleteView,
    CategorieCreateView,
    PostListView,
    PostDetailView,
    PostEditView,
    PostDeleteView,
    PostCreateView,
    LikeView,
    CommentCreateView,
    CommentEditView,
    CommentDeleteView,
    user_posts
)

urlpatterns = [
    path('', CategorieListView.as_view(), name="list-categories"),
    path('<int:pk>/', CategorieDetailView.as_view(), name="category-detail"),
    path("<int:pk>/edit/", CategorieEditView.as_view(), name="category_edit"),
    path("<int:pk>/delete/", CategorieDeleteView.as_view(), name="category_delete"),
    path("new/", CategorieCreateView.as_view(), name="category_create"),
    path('<int:categorie_id>/posts/', PostListView.as_view(), name='post_list'),
    path("<int:categorie_id>/posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:categorie_id>/posts/<int:post_id>/like/<int:pk>", LikeView, name="like_post"),
    path('<int:categorie_id>/posts/<int:post_id>/comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('<int:categorie_id>/posts/<int:post_id>/<int:pk>/comment_edit/', CommentEditView.as_view(), name='comment_edit'),
    path('<int:categorie_id>/posts/<int:post_id>/<int:pk>/comment_delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path("<int:categorie_id>/posts/<int:pk>/edit/", PostEditView.as_view(), name="post_edit"),
    path("<int:categorie_id>/posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("<int:categorie_id>/posts/new/", PostCreateView.as_view(), name="post_new"),  # new
    path('user_posts/', views.user_posts, name='user_posts'),

]
