from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.

def home(request):
    return redirect('/student_list')

def stud_list(request):
    context = {
        'student_list': Student.objects.all()
    }
    return render(request, 'student_list.html', context)

def stud_reg(request, id=0):
    if request.method=='GET':
        if id==0:
            form = StudentForm()
        else:
            stude = Student.objects.get(pk=id)
            form = StudentForm(instance=stude)
        return render(request, 'student_registration.html', {'form': form})
    else:
        if id==0:
            form = StudentForm(request.POST)
        else:
            stude = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=stude)
        if form.is_valid():
            form.save()
        return redirect('/student_list')


def stud_del(request, id):
    stude = Student.objects.get(pk=id)
    stude.delete()
    return redirect('/student_list')