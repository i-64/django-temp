from django.urls import path
from .views import *

urlpatterns = [
    path('test', test, name='test'),
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', logout1, name='logout1'),
]
