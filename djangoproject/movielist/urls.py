from django.urls import path
from . import views

urlpatterns=[
    path('movies/',views.movies,name='movies'),
    path('details/<int:id>',views.details,name='details'),
    path('add/', views.add_movie, name='addmovie'),
    path('', views.movies_list, name='movieslist'),
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('delete/', views.delete_list, name='deletelist'),
    path('update/', views.update_list, name='updatelist'),
    path('update/<int:movie_id>/', views.update_movie, name='update_movie'),
]