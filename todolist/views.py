from django.http import HttpResponse
from django.shortcuts import render, redirect
from todolist.models import tasklist
from todolist.forms import taskfrom
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = taskfrom(request.POST or None)

        if form.is_valid():
            form.save(commit=False).manager = request.user
            form.save()

        messages.success(request, "New Task Added Successfully")
        return redirect('todolist')

    else:
        all_tasks = tasklist.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {"all_task": all_tasks})


def index(request):
    context = {
        'welcome_text': 'Welcome to ToDo-List Page'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'welcome_text': 'Welcome to About Page'
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'welcome_text': 'Welcome to Contact Page'
    }
    return render(request, 'contact.html', context)


@login_required
def delete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request, "Access Prohibited")

    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = tasklist.objects.get(pk=task_id)
        form = taskfrom(request.POST or None, instance=task)

        if form.is_valid():
            form.save()

        messages.success(request, "Task Edited Successfully")
        return redirect('todolist')

    else:
        task_obj = tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {"task_obj": task_obj})


@login_required
def complete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, "Access Prohibited")

    return redirect('todolist')


@login_required
def pending_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, "Access Prohibited")

    return redirect('todolist')
