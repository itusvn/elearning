from django.urls import path
from . import views
from apps.basebackend import views_table

app_name = 'quiz'

urlpatterns = [
    path('category', views_table.TableView.as_view(), name='quiz-category'),
]
