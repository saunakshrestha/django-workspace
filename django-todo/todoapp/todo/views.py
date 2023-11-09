from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_index(request):
    todos = Todo.objects.all().order_by('-creation_date')
    form = TodoForm()
    if (request.method == 'POST'):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        'todos': todos,
        'form': TodoForm(),
    }
    return render(request,'index.html',context)

def todo_detail(request,pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo':todo,
    }
    return render(request,'detail.html',context)
