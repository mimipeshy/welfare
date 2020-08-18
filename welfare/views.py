from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration


# Create your views here.
def login(request):
    return render(request, 'welfare/login.html')


def dashboard(request):
    return render(request, 'welfare/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login-page')
    else:
        form = UserRegistration()
    return render(request, 'welfare/register.html', {'form': form})
