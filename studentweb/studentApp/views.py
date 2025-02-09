from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import StudentForm
from .models import Student


# Home page displaying students
def index(request):
    return render(request, 'student/index.html', {
        'students': Student.objects.all()
    })


# View a single student
def view_student(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'student/view.html', {'student': student})


# Add a new student
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()

            # Send email after saving the student
            send_mail(
                "Welcome to Our System",
                f"Dear {new_student.first_name},\n\nYou have been successfully registered.",
                settings.EMAIL_HOST_USER,
                [new_student.email],
                fail_silently=False,
            )

            return render(request, 'student/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()

    return render(request, 'student/add.html', {'form': form})


# Edit student details
def edit(request, id):
    student = get_object_or_404(Student, pk=id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student/edit.html', {'form': form})


# Delete student
def delete(request, id):
    student = get_object_or_404(Student, pk=id)
    
    if request.method == 'POST':
        student.delete()
    
    return HttpResponseRedirect(reverse('index'))
