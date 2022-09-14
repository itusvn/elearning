from django.shortcuts import render
from apps.basebackend.views_table import TableView
# Create your views here.

class Category(TableView):
    template_name = 'quiz/category/index.html'