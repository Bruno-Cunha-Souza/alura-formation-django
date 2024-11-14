from django.contrib import admin
from school.models import Student, Course, Registration

class StudentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'cpf', 'data_birth', 'cellphone')
	list_display_links = ('id','name', 'email')
	list_per_page = 10
	search_fields = ('name', 'email', 'cpf')

admin.site.register(Student, StudentsAdmin)

class CoursesAdmin(admin.ModelAdmin):
	list_display = ('id', 'code', 'description', 'nivel')
	list_display_links = ('id', 'code', 'description')
	list_per_page = 10
	search_fields = ('code', 'description')
 
admin.site.register(Course, CoursesAdmin)

class RegistrationsAdmin(admin.ModelAdmin):
	list_display = ('id', 'student', 'course', 'period', 'registration_date')
	list_display_links = ('id', 'student', 'course')
	list_per_page = 10

admin.site.register(Registration, RegistrationsAdmin)