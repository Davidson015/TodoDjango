from django.shortcuts import redirect, render
from app.models import Todo
from app.forms import TodoForm

# Create your views here.
# HomePage
def index(request):
    items = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
    
    context = {
        "form": form,
        "items": items
    }
    return render(request, 'index.html', context)

#UpdatePage
def updateitem(request, pk):
    item = Todo.objects.get(id=pk)
    form = TodoForm(instance=item)

    if request.method == 'POST':
        form = TodoForm(request.POST or None, instance=item)
        if form.is_valid():
            item.is_updated = True
            form.save()
            return redirect('home')
    

    context = {
        "form": form,
    }
    return render(request, 'update.html', context)

#DeletePage
def deleteitem(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()

    return redirect('home')
    

    # Uncomment these next lines of code if you want to make use of the "delete.html" template
    # context = {
    #     "item": item
    # }
    # return render(request, 'delete.html', context)