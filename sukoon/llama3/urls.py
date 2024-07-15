from django.urls import path
from . views import respond

urlpatterns = [
    path('', respond, name="respond"),
]