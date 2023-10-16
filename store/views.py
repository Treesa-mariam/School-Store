

# Create your views here.
from django.shortcuts import render, redirect


from store.models import Department


def home(request):
    departments = Department.objects.all()
    return render(request, "home.html")


def department_wikipedia(request, department_id):
    department = Department.objects.get(pk=department_id)
    return redirect(department.wikipedia_link)


