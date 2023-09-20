from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': "Актрисы"},
    {'id': 2, 'name': "Певицы"},
    {'id': 3, 'name': "Спортсменки"}
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', context={'title': 'О сайте', 'menu': menu})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id: {post_id}')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)
