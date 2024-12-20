from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, 'students/index.html', {
        'Students': Student.objects.all()
    })
