from django.shortcuts import render

from .models import (Subscription, Manager, Department, Title)


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_Managers = Manager.objects.filter(status='+').count()
    num_Subscriptions = Subscription.objects.count()  # Метод 'all()' применён по умолчанию.
    num_Departments = Department.objects.count()  # Метод 'all()' применён по умолчанию.
    num_Titles = Title.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_Managers': num_Managers,
                 'num_Subscriptions': num_Subscriptions,
                 'num_Departments': num_Departments,
                 'num_Titles': num_Titles,

                 },
    )


from django.views import generic


class ManagerListView(generic.ListView):
    model = Manager

    context_object_name = 'manager_list'  # имя переменной контекста в шаблоне
    queryset = Manager.objects.filter(status='+')[:5]  # Получение 5 актальных менеджера
    template_name = 'managers/template_manger_list.html'  # Определение имени шаблона и его расположения


class ManagerDetailView(generic.DetailView):
    model = Manager