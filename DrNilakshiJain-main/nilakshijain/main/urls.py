from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.index, name="Home View"),
    path("books/<int:book_id>", views.book, name="Book View"),
]
