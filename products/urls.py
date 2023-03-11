from django.urls import path
from products import views

urlpatterns = [
    path("", views.index, name="index"),
    path("favourite", views.favourite, name="favourite"),
]
