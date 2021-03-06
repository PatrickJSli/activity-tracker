from django.urls import path

from . import views

app_name="projects"
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('projects/<slug:slug>/delete', views.delete_project, name='delete_project'),
]
