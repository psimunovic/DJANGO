from multiprocessing import context
from django.shortcuts import render

from univ_app.models import Student
from . models import Student
# Create your views here.
def index(request):
    estudiantes=Student.objects.all()
    context= {'clase': 'aprendiendo django', 'estudiantes': estudiantes}
    return render(request, 'students_list.html', context)