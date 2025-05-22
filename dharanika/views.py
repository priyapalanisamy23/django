from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'index.html')


def student_form(request):
    if request.method =='POST':
        name=request.POST.get('name')
        roll_number=request.POST.get(roll_number)
        email=request.POST.get('email')
        student.object.create(name=name,roll_number=roll_number,email=email)
        return redirect('student_form')
    students=student.object.all()
    return render(request,'index.html', {'students':students})
    