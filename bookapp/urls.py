from django.urls import path
from . import views

urlpatterns = [
    path('list', views.book_list),
    path('form', views.book_form),
    path('<int:id>/detail', views.book_detail),
    path('<int:id>/edit', views.book_edit),
    path('<int:id>/delete', views.book_delete),
]
