from django.urls import path, include
from . import views

app_name = 'authenticate'

urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('signup/', views.signup, name='signup')),
]
