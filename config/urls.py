from django.contrib import admin
from django.urls import path, include

from apps.quiz import views as views_quiz


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('apps.quiz.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('authenticate/', include('apps.authenticate.urls')),
    path('', views_quiz.home),
]
