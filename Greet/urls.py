from .views import (
    hello
)
from django.urls import path

urlpatterns = [
    path("", hello, name="hello")
]