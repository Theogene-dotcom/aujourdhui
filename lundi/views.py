from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(request,'welcome to kigali coding.com')
