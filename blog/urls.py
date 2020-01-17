from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
      # Look for an integer after the /blog and save it as blog_id
    path('<int:blog_id>/', views.detail, name='detail'),

]
