from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from projects.models import Project

# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'projects/dashboard_noauth.html')

    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/dashboard.html', {'projects' : projects})
