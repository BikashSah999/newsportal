from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoreis/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('fullpost/<int:id>', views.fullpost, name='fullpost'),
    path('trendingpost/', views.trendingpost, name='trendingpost'),
    path('searchpost/', views.searchpost, name='searchpost'),
    path('technology/', views.technology, name='technology'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('news/', views.news, name='news'),
    path('sports/', views.sports, name='sports'),
    path('politics/', views.politics, name='politics'),
    path('blog/', views.blog, name='blog')
]