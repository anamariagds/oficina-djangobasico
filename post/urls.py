from django.urls import path
from post import views


urlpatterns = [
    path('', views.home),
    path('lista_posts/', views.lista_post, name="lista_pos"),
]