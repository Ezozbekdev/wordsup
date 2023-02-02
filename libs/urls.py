from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('register/', register, name='register'),
    # learn
    path('learn/', learn_view, name='learn'),
    # word
    path('word/', word, name='word'),
    path('about/', about_view, name='about')
]