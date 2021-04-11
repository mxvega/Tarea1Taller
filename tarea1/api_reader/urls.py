from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character', views.character_page, name='character'),
    path('BB/', views.season_page_bb, name='BB'),
    path('Breaking/<str:pk>/', views.BreakingBad_id, name='episodesbb'),
    path('BetterCallSaul/', views.season_page_bcs, name='BetterCallSaul'),
    path('BCS/<str:pk>/', views.BetterCallSaul_id, name='episodes_bcs'),
    path('Episode/<str:pk>/', views.Episode_id, name='episodes_info'),
    path('personaje/<str:pk>/', views.Personaje_id, name='personaje_info'),


]