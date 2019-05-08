from django.shortcuts import render, redirect
from .models import Save

# Create your views here.
def home(request):
    return render(request, 'home.html')

def submit(request):
    s = Save()
    s.saving = request.GET['saving']
    s.save()
    return redirect('/')
