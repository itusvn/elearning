from django.urls import path

from apps.basebackend import views_table
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('tables', views_table.TableView.as_view(), name='table'),
]
