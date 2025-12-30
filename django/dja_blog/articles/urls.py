from django.urls import path
from .views import article_list, category_list, category_articles, article_detail, article_create, article_edit, article_delete

urlpatterns = [
    path('', article_list, name='article_list'),
    path('category/', category_list, name='category_list'),
    path('category/<int:pk>/', category_articles, name='category_articles'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/new/', article_create, name='article_new'),
    path('article/<int:pk>/edit/', article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
]
