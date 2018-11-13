from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    data = Job.objects
    return render(request,'jobs/home.html',{'jobs':data})
