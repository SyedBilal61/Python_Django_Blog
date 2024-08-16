from django.shortcuts import render, HttpResponse, redirect
from .models import Events, Role, Department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def all_evn(request):
    evns = Events.objects.all()
    for evn in evns:
        print(f"ID: {evn.id}, First Name: {evn.first_name}, Last Name: {evn.last_name}, Role: {evn.role}, Department: {evn.dept}, Booking Date: {evn.book_date}")
        print(evns)
    context = {
        'evns': evns
    }
    print(context)
    return render(request, 'all_evn.html', context)

@login_required(login_url='login')
def add_evn(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        role = request.POST.get('role', '')
        dept = request.POST.get('dept', '')
        book_date = datetime.now().date()  # Using current date instead of form date

        new_evn = Events(
            first_name=first_name, 
            last_name=last_name, 
            dept=dept, 
            role=role, 
            book_date=book_date
        )
        new_evn.save()
        return HttpResponse('Event registered Successfully')
    elif request.method == 'GET':
        return render(request, 'add_evn.html')
    else:
        return HttpResponse('An exception occurred! Event Not added')

@login_required(login_url='login')
def remove_evn(request, evn_id=0):
    if evn_id:
        try:
            evn_to_be_removed = Events.objects.get(id=evn_id)
            evn_to_be_removed.delete()
            return HttpResponse("Event Cancelled Successfully")
        except Events.DoesNotExist:
            return HttpResponse("Event not found. Please enter a valid Event ID.")

    evns = Events.objects.all()
    context = {
        'evns': evns
    }
    print(context)
    return render(request, 'remove_evn.html', context)

@login_required(login_url='login')
def filter_evn(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')

        # Start with all events
        evns = Events.objects.all()

        # Apply filters based on the provided data
        if name:
            evns = evns.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            evns = evns.filter(dept__icontains=dept)  # Correctly filter by department name
        if role:
            evns = evns.filter(role__icontains=role)  # Correctly filter by role name

        # Prepare context and render the result
        context = {
            'evns': evns
        }
        return render(request, 'all_evn.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_evn.html')

    else:
        return HttpResponse('An exception occurred!')







#login-page views here 

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2 :
            return HttpResponse("Password and Confirm Password are different Please write correct password")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login') 
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is Incorrect")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect ('login')
