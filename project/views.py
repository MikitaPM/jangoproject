from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'project/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return HttpResponse('project/about.html')

def create(request):
    return HttpResponse('project/create.html')
# Create your views here.
