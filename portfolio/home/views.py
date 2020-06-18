from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    context = {
        'experienceobj': models.experience.objects.all(),
        'educationobj': models.education.objects.all(),
        'awardsobj' : models.awards.objects.all(),
        'projectobj' : models.project.objects.all()
    }
    return render(request,template_name='index.html',context = context)


