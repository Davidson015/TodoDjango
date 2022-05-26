# from multiprocessing import context
from django.shortcuts import render
from app.models import Todo
from app.forms import TodoForm

# Create your views here.
def index(request):
    items = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid:
            form.save()
    
    form = TodoForm()
    context = {
        "form": form,
        "items": items
    }
    return render(request, 'index.html', context)
