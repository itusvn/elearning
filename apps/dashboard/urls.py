from django.urls import path
from . import views_table
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('tables', views_table.TableView.as_view(), name='table'),
]
