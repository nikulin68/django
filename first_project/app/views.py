import datetime
import time


from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from os import listdir
from os.path import isfile,join

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('online time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)



def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time_date = datetime.datetime.now()
    current_time = current_time_date.time()
    msg = f'Текущее время : {current_time}'
    return HttpResponse(msg)



def workdir_view(request):
    cwd = os.getcwd()
    res = os.listdir(path=cwd)



    files =f'Список файлов{res}'
    return HttpResponse(files)
