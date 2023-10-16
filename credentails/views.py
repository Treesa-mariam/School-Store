from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('user_profile')
        else:
            messages.info(request,"invalid credentails")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username takes")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email takes")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user registered")
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect("register")
        return redirect('/')
    return render(request,"register.html")


from django.shortcuts import render

@login_required
def user_profile(request):
    message = ""
    if request.method == "POST":
        # Process the form data here
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        department = request.POST.get("department")
        courses = request.POST.get("courses")
        purpose = request.POST.get("purpose")
        materials = request.POST.getlist("materials")
        # user = auth.authenticate(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,department=department,courses=courses,purpose=purpose,materials=materials)
        # user.save()

        # Perform any necessary processing (e.g., save to the database)

        # Set the confirmation message
        message = "Order Confirmed"

    return render(request, "user_profile", {'message': message})


def logout(request):
    auth.logout(request)
    return redirect('/')