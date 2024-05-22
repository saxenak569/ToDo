from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo, name="todo"),
    path("login/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("signout/", views.signout, name="signout"),
    path("Users/", views.users, name="users"),
    path("Users/details/<int:id>", views.details, name="details"),
    path("Users/details/delete/<int:id>", views.delete_todo, name="delete_todo"),
]
