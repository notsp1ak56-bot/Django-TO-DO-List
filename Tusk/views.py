from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from  django.contrib.auth.models import User
from .models import *
from .forms import *
from  django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

# Создаем тут функцию которая базу данных и вынимает из нее все
@login_required
def main(request):
    data_center = Tusks.objects.filter( owner = request.user)
    #  тут создаем словарь потому что  метод render принимает  ключ значение поэтому зарание запехнули его  в словарь
    data = {
        "tusks":data_center
        }
    return  render(request,"Tusk/main.html", data)

# добавляем  дикаратор что бы  не выводило ошибку при не зареганом пользователю
@login_required
# создаем функцию которая принмает ответ от браузера
def add_tusk(request):
    if request.method == "POST":
        form = TuskForm(request.POST)
        # выше строчкой мы берем то что передал на пользователь в  POST
        if form.is_valid():
            tusk = form.save(commit=False)
            # пишем что берем  эту форму но не вносим пока что в базу данныъ
            tusk.owner = request.user
            # Привязываем  эту  задачу к пользователю
            form.save()
            return redirect('main')
    # Отрисововаем просто форму
    else:
        form = TuskForm()

    return render(request,"Tusk/add_tusk.html",{"form":form})
# создаем  функцию для изменение задач
@login_required
def edit_tusk(request,tusk_id):
    # прописоваем строкой ниже  что берем в Tusks id  задачи и пользователя которой привазан к этой задаче
    task = get_object_or_404(Tusks, id = tusk_id, owner=request.user)

    if request.method == "POST":
        # обновляем таблицу
        form = TuskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect("main")
    # просто пишем что обновляем задачу в форме
    else:
        form = TuskForm(instance=task)
    return render(request,"Tusk/edit_tusk.html",{"form":form})

# создаем функцию по удалению это функции
@login_required
def delete_tusk(request, tusk_id):
    tusks = get_object_or_404(Tusks, id = tusk_id , owner = request.user)
    if request.method == "POST":
        # Удаление задачу
        tusks.delete()
        return redirect('main')

    return render(request, "Tusk/delete_tusk.html", {"tusks": tusks})
# создаем функцию профиль
def profile(request):
    # берем именно те данные что лежат у пользователя
    task = Tusks.objects.filter(owner = request.user)
    # просто общее количество
    total_task = task.count()
    #  не решенные задачи фильтруем смопощью метода филтер  и выыводим его количество
    unresolved = task.filter(is_completed = False).count()
    # с этим методом так же
    done_task = task.filter(is_completed = True).count()

    data = {
        "task":task,
        "total_task": total_task,
        "unresolved":unresolved,
        "done_task": done_task

    }

    return render(request, "Tusk/profile.html", data)
# отмечаем задачу что решенна
def coplete_tusk(request , tusk_id):
    tusk = get_object_or_404( Tusks,owner = request.user  ,id = tusk_id)
    # пишем что
    tusk.is_completed = not tusk.is_completed

    tusk.save()
    return redirect('main')
#сделать функцию
#def  search(request):

# сделать сортировку по важности задачи
#def важность(request):

# сделать что бы страницы листались
#def  page_move(request):

#надо как то сделать что бы важность как регулировалась по важности высокий приотет средний и низки !!!!!!!!!!

# cоздаем форму регестриции
class SingnUpwiew(CreateView):
    # создаем  форму как раз
    form_class = UserCreationForm
    # после регистрации куда возращяем
    success_url = reverse_lazy('login')
    #  и сылка грубо говоря на   html файл с регистрацией
    template_name = 'registration/signup.html'

