from django.shortcuts import render,redirect
from .models import Truck


def home(request):
    trucks = Truck.objects.all()
    context = {
        'trucks':trucks
    }
    return render(request,'brands/index.html',context)
