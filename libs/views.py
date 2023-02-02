from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .models import Word, About

def redirect_if_not_logged_in(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrap

def about_view(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'html/about.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'html/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'html/register.html', {'form': form})
def home(request):
    return render(request, 'html/index.html')

@redirect_if_not_logged_in
def learn_view(request):
    return render(request, 'html/learn.html')

def word(request):
    level = request.GET.get('level')
    if level:
        words = Word.objects.filter(level=level)
        return render(request, 'html/word.html', {'words': words})
    else:
        return redirect('learn')
