from django.db import models

# Create your models here.

class Student(models.Model):
    student_number = models.PositiveIntegerField()  # Corrected 'pasitiveIntegerField' to 'PositiveIntegerField'
    first_name = models.CharField(max_length=100)   # Fixed 'max_length=100' formatting
    last_name = models.CharField(max_length=50)     # Fixed 'max_length=50' formatting
    email = models.EmailField(max_length=100)       # Fixed 'models.emailField' to 'models.EmailField'
    field_of_study = models.CharField(max_length=50)  # Fixed 'max_length=50' formatting
    gpa = models.FloatField()  
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'


