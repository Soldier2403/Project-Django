from django.urls import path
from website import views

urlpatterns = [
    path('http_test', views.http_test),
]
