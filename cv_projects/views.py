from django.shortcuts import render
from django.http import HttpResponse
from cv_projects.models import Project

# Create your views here.
def project_list(request):
    return render(request, 'cv_projects/index.html')

def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'cv_projects/all_projects.html', {"projects": projects})
