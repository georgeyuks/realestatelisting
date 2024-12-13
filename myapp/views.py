from django.shortcuts import render, redirect
from django.template.context_processors import request

from myapp.models import User,Message,Book



# Create your views here.
def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        ).exists():
            return render(request, 'index.html')

        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def message(request):
    if request.method == 'POST':
        # Extract form data
        mymessage = Message(
        name = request.POST['name'],
        email = request.POST['email'],
        subject = request.POST['subject'],
        message = request.POST['message']
        )
        mymessage.save()

        # Redirect after successful save
        return redirect('/about')
    else:
        # Render the contact page for GET requests
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    return render(request, 'contact.html')

def properties(request):
    return render(request, 'properties.html')

def book(request):
    if request.method == 'POST':
        # Create a new Book instance with form data
        mybook = Book(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            message = request.POST['message']
        )
        # Save the instance to the database
        mybook.save()

        # Redirect to the contact page after saving
        return redirect('/services')

    else:
        # Render the contact page for GET requests
        return render(request, 'book.html')




def service(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def register(request):
    if request.method == 'POST':
        members = User(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')


def property(request):
    return render(request, 'property-single.html')







