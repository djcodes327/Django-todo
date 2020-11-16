from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        registrationForm = CustomRegisterForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            messages.success(request, "User Registered Successfully")
            return redirect('todolist')

    else:
        registrationForm = CustomRegisterForm()
    return render(request, 'register.html', {"registrationForm": registrationForm})
