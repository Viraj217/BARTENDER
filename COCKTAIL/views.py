from django.shortcuts import render
from django.http import HttpResponse
import requests 
from .forms import DRINKFORM
from .forms import INGREDIENTFORM

def home(request):
    return render(request, 'COCKTAIL/index.html')

def bartender_view(request):
    return HttpResponse("Bartender View Page")

def drink_form(request):
    form = DRINKFORM(request.GET or None)
    results = []

    if form.is_valid():
        drink = form.cleaned_data['drink'] 
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}'
        response = requests.get(url)
        data = response.json()

        if data['drinks']:
            for d in data['drinks']:
                results.append({
            'name': d['strDrink'],
            'category': d['strCategory'],
            'instructions': d['strInstructions'],
            'image': d['strDrinkThumb'],
        })


    return render(request, 'COCKTAIL/search.html', {'form': form, 'results': results})

def ingredient_form(request):
    form = INGREDIENTFORM(request.GET or None)
    results = []

    if form.is_valid():
        ingredient = form.cleaned_data['ingredient'] 
        url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}'
        response = requests.get(url)
        data = response.json()

        if data['drinks']:
            for d in data['drinks']:
                results.append({
            'name': d['strDrink'],
            'image': d['strDrinkThumb'],
        })


    return render(request, 'COCKTAIL/search.html', {'form': form, 'results': results})
