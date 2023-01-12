from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'project/index.html', {'title': 'Главная страница', 'task': tasks})


def about(request):
    return render(request, 'project/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не заполнена"

    form = TaskForm
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'project/create.html', context)
# Create your views here.
