from django.urls import path

from .views import TodoList, TodoDetail

urlpatterns = [
    path('<int:pk>/', TodoDetail.as_view(), name="todo_detail"),
    path('', TodoList.as_view(), name="todo_list"),
]