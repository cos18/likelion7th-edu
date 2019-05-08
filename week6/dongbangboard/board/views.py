from django.shortcuts import render, redirect
from .models import Message

# Create your views here.
def home(request):
    messages = Message.objects
    return render(request, 'home.html', {'messages':messages})

def submit(request):
    message = Message()
    message.words = request.GET['words']
    message.writter = request.GET['writter']
    message.date = request.GET['date']
    message.save()
    return redirect('/')