from django.urls import path
from .views import *
app_name = 'core'

urlpatterns = [
    path('',Home.as_view())
]