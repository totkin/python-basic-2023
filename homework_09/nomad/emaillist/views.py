from django.db.models import Q
from django.shortcuts import render

from .models import (Subscription, Manager, Department, Title)


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

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
                 'num_visits':num_visits
                 },
    )


from django.views import generic


class ManagerListView(generic.ListView):
    model = Manager

    context_object_name = 'manager_list'  # имя переменной контекста в шаблоне
    # queryset = Manager.objects.filter(status='+')[:5]  # Получение 5 актуальных менеджеров
    template_name = 'managers/template_manger_list.html'  # Определение имени шаблона и его расположения

    paginate_by = 10

    # context_object_name = 'all_search_results'
    def get_queryset(self):
        result = super(ManagerListView, self).get_queryset()
        query = self.request.GET.get('search')
        print(query)
        if query:
            postresult = Manager.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
            # помни почему в sqlite не работает нормально бпоиск без учета регистра!!!
            # https://docs.djangoproject.com/en/2.1/ref/databases/#sqlite-string-matching
            result = postresult
        else:
            result = Manager.objects.filter(status='+')
        return result


class ManagerDetailView(generic.DetailView):
    model = Manager


class DepartmentDetailView(generic.DetailView):
    model = Department


class DepartmentListView(generic.ListView):
    model = Department


class TitleDetailView(generic.DetailView):
    model = Title


class TitleListView(generic.ListView):
    model = Title


class SearchView(generic.ListView):
    model = Manager
    template_name = 'manager_list.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Manager.objects.filter(first_name__icontains=query)
            result = postresult
        else:
            result = None
        return result
