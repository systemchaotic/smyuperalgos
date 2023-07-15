```python
from django.shortcuts import render
from .models import Content
from .forms import ContentForm

def index(request):
    contents = Content.objects.all()
    return render(request, 'index.html', {'contents': contents})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    contents = Content.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'contents': contents})

def content_create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.author = request.user
            content.save()
            return redirect('dashboard')
    else:
        form = ContentForm()
    return render(request, 'content_form.html', {'form': form})

def content_edit(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            content = form.save()
            return redirect('dashboard')
    else:
        form = ContentForm(instance=content)
    return render(request, 'content_form.html', {'form': form})

def content_delete(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        content.delete()
        return redirect('dashboard')
    return render(request, 'content_confirm_delete.html', {'content': content})
```