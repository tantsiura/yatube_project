from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница с постами,отфильтрованными по группам
def group_posts(request, slug):
    return HttpResponse('Здесь будут отображены группы постов. {slug}')


