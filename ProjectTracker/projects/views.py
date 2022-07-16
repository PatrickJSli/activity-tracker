from time import time
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from slugify import slugify

from projects.models import Project, ProjectForm, Session, SessionForm, Milestone, MilestoneForm

# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'projects/dashboard_noauth.html')

    if request.method == 'POST':
        project = Project(owner=request.user)
        formset = ProjectForm(request.POST, instance=project)
        if formset.is_valid():
            new_project = formset.save(commit=False)
            new_project.slug = slugify(project.title)
            formset.save()
    else:
        formset = ProjectForm()

    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/dashboard.html', {'projects' : projects, 'formset' : formset})

def project_detail(request, slug):
    project = Project.objects.filter(owner=request.user).get(slug=slug)
    sessions = Session.objects.filter(project=project)
    milestones = Milestone.objects.filter(project=project)

    if request.method == 'POST':
        if request.POST['type'] == 'session':
            session = Session(project=project)
            formset = SessionForm(request.POST, instance=session)
            project.last_worked_on=request.POST['end_date']
            if formset.is_valid():
                formset.save()
                project.save()
        elif request.POST['type'] == 'milestone':
            milestone = Milestone(project=project)
            formset = MilestoneForm(request.POST, instance=milestone)
            if formset.is_valid():
                formset.save()
            
    return render(request, 'projects/project_detail.html', {'project' : project, 'sessions' : sessions, 'milestones' : milestones})
