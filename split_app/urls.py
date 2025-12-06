from django.urls import path
from split_app.views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegistrationView.as_view(), name='register'),
]