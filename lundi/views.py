from django.shortcuts import render

def index(request):
    return HttpResponse(request,'welcome to kigali coding')
