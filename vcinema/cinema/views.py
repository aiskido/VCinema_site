from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Movies, Comments
from .forms import CommentsForm


def index(request):
    movies = Movies.objects.all()[:10]
    context = {
        'movies': movies,
    }
    return render(request, "cinema/index.html", context)


def detail(request, pk):
    movie = Movies.objects.get(id=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        username = request.user.username
        f = {
            'name': username,
            'movie': movie,
            'comment': request.POST['comment']
        }
        form = CommentsForm(f)
        if form.is_valid():
            form.save()
        return redirect(reverse("cinema:detail", args=(pk, )))

    comments = Comments.objects.filter(movie__pk=pk)
    context = {
        'movie': movie,
        'comments': comments
    }
    return render(request, "cinema/detail.html", context)


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repass = request.POST['repass']
        if repass == password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user = authenticate(username=username, password=password)
                if user != None:
                    login(request, user)
                    return redirect(reverse("cinema:main"))
                else:
                    return redirect(reverse("cinema:authorize"))
            except Exception as e:
                print(e)
                return redirect(reverse("cinema:register"))
        else:
            return redirect(reverse("cinema:register"))
    return render(request, "cinema/registration.html")


def authorize(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(reverse("cinema:main"))
        else:
            return redirect(reverse("cinema:authorize"))
    return render(request, "cinema/login.html")

def logout_view(request):
    logout(request)
    return redirect(reverse("cinema:main"))