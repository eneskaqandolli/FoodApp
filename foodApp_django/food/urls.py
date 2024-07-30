from django.urls import path, include

from . import views

app_name = 'food'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add", views.AddItemView.as_view(), name="add"),
    path("update/<int:pk>", views.update_item, name="update_item"),
    path("delete/<int:id>", views.delete_item, name="delete"),
    path("<int:pk>", views.DetailFoodView.as_view(), name="detail"),
]
