from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<slug:slug>', views.ArticleView.as_view(), name='article'),
    path('page/<slug:slug>', views.PageView.as_view(), name='page'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='category'),
    path('article/<slug:slug>/comment', views.add_comment, name='add_comment'),
]