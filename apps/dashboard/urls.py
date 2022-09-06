from django.urls import path
from . import views
from . import views_table

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('tables', views_table.TableView.as_view(), name='table'),
]
