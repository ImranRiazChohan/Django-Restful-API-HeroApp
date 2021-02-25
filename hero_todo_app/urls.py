from django.urls import path
from . import views

urlpatterns = [
    path('/',views.Home,name="Home"),
    path('/create_hero/',views.Hero_Create,name="create_hero"),
    path('/hero_update/<str:pk>/',views.Hero_Update,name="hero_update"),
    path('/hero_delete/<str:pk>/',views.Hero_Delete,name="hero_delete"),
    path('/heroes/',views.Hero_list,name="hero_list"),
    path('/hero/<str:pk>/',views.Search_Hero,name="Search_hero"),

]
