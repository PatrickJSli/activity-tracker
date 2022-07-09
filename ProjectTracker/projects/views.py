from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from projects.models import Project, ProjectForm

# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'projects/dashboard_noauth.html')

    if request.method == 'POST':
        project = Project(owner=request.user)
        formset = ProjectForm(request.POST, instance=project)
        if formset.is_valid():
            formset.save()
    else:
        formset = ProjectForm()

    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/dashboard.html', {'projects' : projects, 'formset' : formset})
