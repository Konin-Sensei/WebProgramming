from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mysite.core.models import Puzzle
from .forms import PuzzleForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def sudoku(request):
    if request.method == 'POST':
        if Puzzle.objects.filter(account=request.user).exists():
            instance = Puzzle.objects.get(account=request.user)
            form = PuzzleForm(request.POST, instance=instance)
            if form.is_valid:
                form.save()
                return redirect('home')
            else:
                return redirect('sudoku')
        else:
            Puzzle.objects.create(account=request.user)
            form = PuzzleForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('home')
            else:
                return redirect('sudoku')
    else:
        if Puzzle.objects.filter(account=request.user).exists():
            instance = Puzzle.objects.get(account=request.user)
            form = PuzzleForm(instance=instance)
            return render(request, 'sudoku/sudoku.html', {'form': form})
        else:
            return render(request, 'sudoku/sudoku.html', {'form': PuzzleForm()})
