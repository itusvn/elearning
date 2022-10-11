from django.shortcuts import render, redirect
from apps.basebackend.views_table import TableView
# Create your views here.

class Category(TableView):
    template_name = 'quiz/category/index.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('dashboard')
        elif request.user.is_student:
            return redirect('students:quiz_list')
        else:
            return redirect('admin:index')
    return render(request,'front/index.html')