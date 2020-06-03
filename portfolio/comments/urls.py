from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.articles, name='articles'),
    path('get/<int:article_id>', views.article, name='article'),
    path('addcomment/<int:article_id>', views.addcomment, name='addcomment'),
]
