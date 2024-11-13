from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(blank = False, max_length=40)
  cpf = models.CharField(max_length=11)
  data_birth = models.DateField()
  cellphone = models.CharField(max_length=14)
  
  def __str__(self):
      return self.name

class Course(models.Model):
  NIVEL = (
    ('B', 'Basic'),
    ('I', 'Intermediate'),
    ('A', 'Advanced')
  )
  
  code = models.CharField(max_length=10)
  description = models.TextField(blank = False, max_length=100)
  nivel = models.CharField(max_length=1, choices = NIVEL, blank = False, null = False, default = 'B')

  def __str__(self):
      return self.code  
  
class Registration(models.Model):
  PERIOD = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
  )
  
  student = models.ForeignKey('Student', on_delete = models.CASCADE)
  course = models.ForeignKey('Course', on_delete = models.CASCADE)
  period = models.CharField(max_length=1, choices = PERIOD, blank = False, null = False, default = 'M')
  registration_date = models.DateField(auto_now = True)
