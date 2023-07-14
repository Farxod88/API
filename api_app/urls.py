from django.urls import path
from .views import *

urlpatterns = [
    path('', Test),
    path('post/', Test_post)
]
