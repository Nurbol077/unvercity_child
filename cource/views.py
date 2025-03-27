from django.shortcuts import render
from django.views import generic

from .models import Classes


class ClassesListView(generic.ListView):
    model = Classes
    template_name = 'classes.html'
    context_object_name = 'classes'
