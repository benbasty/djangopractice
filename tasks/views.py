from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks']
    })

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task and task.strip():
            tasks = request.session.get('tasks', [])
            tasks.append(task)
            request.session['tasks'] = tasks
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {'error': 'Task cannot be empty'})
    return render(request, 'tasks/add.html')