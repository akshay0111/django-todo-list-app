from django.shortcuts import render,redirect
from home_to_do.models import *
from home_to_do.forms import *
# Create your views here.
def index(request):
    todo = Todo.objects.all().order_by('-created')
    form = TodoForm

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")



    template_name ='todo/index.html'
    context ={'todo': todo,'form':form}
    return render(request, template_name,context)


def updateTask(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)

    if  form.is_valid():
        form.save()
        return redirect("/")

    context ={'form': form}

    return render(request, 'todo/update_task.html',context)

def deleteTask(request,pk):
    item = Todo.objects.get(id=pk)


    if request.method == 'POST':
        item.delete()
        return redirect("/")






    context = {'item': item}
    return render(request,'todo/delete_task.html',context)
