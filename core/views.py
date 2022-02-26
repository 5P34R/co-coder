from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import Notes

@login_required
def index(request):
    if request.user:
        obj = Notes.objects.filter(user=request.user)[:5]
        context = {
            'posts':obj
        }
    
        return render(request, 'index.html', context)
    return render(request, 'index.html', context)

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


@login_required
def blog(request):
    posts = Notes.objects.filter(user=request.user).order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)

    try:
        obj = paginator.page(page)
    except PageNotAnInteger: 
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    context = {
        'posts':obj
    }
    return render(request, 'blog.html', context)
@login_required
def detailedView(request, slug):
    posts = Notes.objects.get(slug=slug)
    context = {
        'posts':posts,
    }
    return render(request, 'partials/detailView.html', context)

@login_required
def search(request):
    if request.method == 'POST':
        search = request.POST['searched']
        posts = Notes.objects.filter(title__contains=search)
        return render(request, 'blog.html', {'posts':posts})
    else:
        posts = Notes.objects.all()
        return render(request, 'blog.html',{'posts':posts})

@login_required
def add_notes(request):
    if request.method == 'POST':
        title = request.POST['title']
        des = request.POST['des']
        if title and des:
            obj = Notes.objects.create(title=title, description=des, user=request.user)
            # breakpoint()
            obj.save()
        return redirect('/blog')
    return render(request, 'notes/addnote.html')