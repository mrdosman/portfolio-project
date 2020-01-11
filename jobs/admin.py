from django.contrib import admin

# Import the class Job from models.py
from .models import Job

admin.site.register(Job)
