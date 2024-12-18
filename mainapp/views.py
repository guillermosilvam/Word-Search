from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def game(request):
    letter = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    words = [
        'Apple', 'Banana', 'Cat', 'Dog', 'Elephant', 'Frog', 'Giraffe', 'Horse', 'Iguana', 'Jaguar'
    ]    
    
    game = {
        'letter' : letter,
        'words' : words
    }

    

    return render(request, 'game.html', game)
