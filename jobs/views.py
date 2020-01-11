from django.shortcuts import render
# import Job object from models
from .models import Job

def home(request):
    # get all of the objects (jobs) from Job
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
