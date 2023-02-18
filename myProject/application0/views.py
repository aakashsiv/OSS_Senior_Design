import random
from django.shortcuts import render

def coinflip(request):
    result = random.choice(['Heads', 'Tails'])
    return render(request, 'application0.html', {'result': result})
