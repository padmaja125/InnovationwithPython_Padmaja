from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .Forms import FeedbackForm,Name_Form,Id_Form, Address_Form

def test(request):
    return HttpResponse("Hello, world. You're at the test application.")

def trial(request):
    return HttpResponse("You are at the trial")

def html(request):
    form = FeedbackForm()
    context = {'form': form}
    return render(request, "demo.html", context)

def Nameview(request):
    form = Name_Form(request.POST or None)
    if form.is_valid():  # after checking condition
        form.save()
        form = Name_Form()

    context = {'form': form}
    return render(request, "demo.html", context)

def Idview(request):
    form = Id_Form(request.POST or None)
    if form.is_valid():  # after checking condition
        form.save()
        form = Id_Form()

    context = {'form': form}
    return render(request, "demo.html", context)

def Addressview(request):
    form = Address_Form(request.POST or None)
    if form.is_valid():  # after checking condition
        form.save()
        form = Address_Form()

    context = {'form': form}
    return render(request, "demo.html", context)

