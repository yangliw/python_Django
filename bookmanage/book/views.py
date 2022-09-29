from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test_book(request):
    return HttpResponse('ok')