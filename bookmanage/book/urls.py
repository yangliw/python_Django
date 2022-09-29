from django.urls import path
from book.views import test_book

urlpatterns = [
    path('test/',test_book),
]