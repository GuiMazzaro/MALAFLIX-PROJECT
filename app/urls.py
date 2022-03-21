from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("category/", CategoriaAPI.as_view(), name='category'),
    path('category/<int:pk>/', CategoriaAPI.as_view(), name='categoryParameters'),

    path("movies/", MoviesAPI.as_view(), name='movies'),
    path('movies/<int:pk>/', MoviesAPI.as_view(), name='moviesParameters'),

    path("signature/", SignatureAPI.as_view(), name='signature'),
    path('signature/<int:pk>/', SignatureAPI.as_view(), name='signatureParameters'),

    path("users/", UsersAPI.as_view(), name='users'),
    path('users/<int:pk>/', UsersAPI.as_view(), name='usersParameters'),

    path("favorite/", FavoriteAPI.as_view(), name='favorite'),
    path('favorite/<int:pk>/', FavoriteAPI.as_view(), name='favoriteParameters'),
]