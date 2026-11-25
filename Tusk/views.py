from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from  django.shortcuts import *
from django.http import HttpResponse
# Create your views here.

# Создаем тут функцию которая базу данных и вынимает из нее все
def main(request):
    data_center = Tusks.objects.all()
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

