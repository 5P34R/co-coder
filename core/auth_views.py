from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm


def logout_view(request):
    logout(request)
    return redirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # breakpoint()
        user= authenticate(request,username=username, password=password)

        if user is not None:
            form = login(request,user)
            return redirect('/')
        return render(request, 'auth/login.html', {'error':'Invalid Username/Password'})
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('/')
        return render(request, 'auth/signup.html', {'form': form})
    return render(request, 'auth/signup.html')

