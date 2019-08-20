"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'otome_reviews'

urlpatterns = [

    #Home page

    path('', views.index, name='index'),

    # Page that shows all games.

    path('games/', views.games, name='games'),

    # Detail page for a single game.

    path('games/<int:game_id>/', views.game, name='game'),

]
