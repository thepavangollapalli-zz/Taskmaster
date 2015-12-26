from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Task
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
currentUser = None

class Index(generic.View):
    def get(self, request):
        global currentUser
        tasks = currentUser.task_set.order_by("-priority")
        new_set = list(tasks)
        a = new_set.append(currentUser)
        print(new_set)
        context = {"tasks": new_set}
        return render(request, 'todo/index.html', context)

class AddView(generic.View):
    def get(self, request):
        context = {'none': None}
        return render(request, 'todo/add.html', context)

    def post(self, request):
        global currentUser
        user = currentUser #User.objects.get(user_name=request.POST["name"])
        task_name = request.POST["task"]
        priority = request.POST["priority"]
        if(len(request.POST["description"])>0):
            description = request.POST["description"]
        else:
            description = ""
        new_task = user.task_set.create(task_name = task_name, priority=priority, description=description)
        # new_task.save()
        return HttpResponseRedirect(reverse("todo:index"))

class LoginView(generic.View):
    def get(self, request):
        return render(request, 'todo/login.html')

    def post(self, request):
        global currentUser
        name = request.POST["name"]
        if(not User.objects.filter(user_name=name).exists()):
            user = User(user_name = name)
        else:
            user = User.objects.get(user_name = name)
        user.save()
        currentUser = user
        print(currentUser.user_name)
        return HttpResponseRedirect(reverse("todo:index"))

def editView(request):
    global currentUser
    user = currentUser #User.objects.get(user_name = request.POST["name"])
    task = user.task_set.get(task_name = request.POST["task"])
    context={"task" : task}
    return render(request, "todo/edit.html", context)

def update(request):
    global currentUser
    user = currentUser #request.POST["name"]
    task_name = request.POST["task"]
    task = user.task_set.get(task_name = request.POST["old_task"])
    if(task_name != task.task_name):
        task.task_name = task_name
    elif(request.POST["priority"] != task.priority):
        task.priority = request.POST["priority"]
    elif(request.POST["description"] != task.description):
        task.description = request.POST["description"]
    task.save()
    return HttpResponseRedirect(reverse("todo:index"))

def delete(request):
    global currentUser
    obj = currentUser.task_set.get(task_name = request.POST["task"])
    obj.delete()
    return HttpResponseRedirect(reverse("todo:index"))