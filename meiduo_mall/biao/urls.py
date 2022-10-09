from django.urls import path
from biao import views

urlpatterns = [
    path('test', views.Test.as_view())
]