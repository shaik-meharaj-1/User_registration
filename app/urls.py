from django.urls import path
from .views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('verify',verify,name='verify'),
    path('home',home,name='home'),
    path('signin',signin,name='signin'),
    path('logout',logout,name='logout'),
    path('forgot',forgot,name='forgot'),
    path('password_change',password_change,name='password_change')
]
