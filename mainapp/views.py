from django.shortcuts import render
import random, string

def home(request):
    return render(request, 'home.html')

def game(request):
    

    words = [
        'Apple', 'Banana', 'Cat', 'Dog', 'Elephant', 'Frog', 'Giraffe', 'Horse', 'Iguana', 'Jaguar'
    ]    

    letters_num = 285
    def letters_generator(letters_num):
        letter = []
        for i in range(letters_num):
            letters = random.choice(string.ascii_lowercase)
            letter.append(letters)
        return letter
    
    letters = letters_generator(letters_num)
    
    
    game = {
        'letters' : letters,
        'words' : words
    }

    

    return render(request, 'game.html', game)
