from django.urls import path, include
from . import views

app_name = 'authenticate'

urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('login/', views.mylogin, name='login'),
   path('register/', views.register, name='register'),
   path('forget-password/', views.forgetpassword, name='forget-password'),
]
