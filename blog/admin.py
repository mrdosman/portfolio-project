from django.contrib import admin

# Import the class Blog from models.py
from .models import Blog

admin.site.register(Blog)
