from django.shortcuts import render,redirect


def home(request):
    context = {}
    return render(request,'brands/index.html',context)
