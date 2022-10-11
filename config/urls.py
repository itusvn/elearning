from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('apps.quiz.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('authenticate/', include('apps.authenticate.urls')),
]
