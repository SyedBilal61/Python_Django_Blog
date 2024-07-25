from django.shortcuts import render, HttpResponse
from .models import Events, Role, Department
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def all_evn(request):
    evns = Events.objects.all()
    context = {
        'evns': evns
    }
    print(context)
    return render(request, 'all_evn.html', context)

def add_evn(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        role_id = request.POST.get('role', '')
        dept_id = request.POST.get('dept', '')
        book_date = datetime.now().date()  # Using current date instead of form date

        new_evn = Events(
            first_name=first_name, 
            last_name=last_name, 
            dept_id=dept_id, 
            role_id=role_id, 
            book_date=book_date
        )
        new_evn.save()
        return HttpResponse('Event registered Successfully')
    elif request.method == 'GET':
        return render(request, 'add_evn.html')
    else:
        return HttpResponse('An exception occurred! Event Not added')

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
            evns = evns.filter(dept__name__icontains=dept)  # Correctly filter by department name
        if role:
            evns = evns.filter(role__name__icontains=role)  # Correctly filter by role name

        # Prepare context and render the result
        context = {
            'evns': evns
        }
        return render(request, 'all_evn.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_evn.html')

    else:
        return HttpResponse('An exception occurred!')
