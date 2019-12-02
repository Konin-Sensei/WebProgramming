from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mysite.core.models import Puzzle

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sudoku(request):
    return render(request, 'sudoku/sudoku.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def sudoku(request):
    if request.method == 'POST':
        form = Puzzle(request.POST)
        if form.is_valid():
            return render(request, 'home.html')
    else:
        puzzles = Puzzle.objects.get(player=request.user)
        args = {'Puzzle': puzzles}
        return render(request, 'sudoku/sudoku.html', args)