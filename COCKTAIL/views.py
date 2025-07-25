from django.shortcuts import render
from django.http import HttpResponse
import requests 
from .forms import DRINKFORM
from .forms import INGREDIENTFORM
from .models import drink_model

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

        obj ,_ = drink_model.objects.get_or_create(drink_name=drink)
        obj.drink_count += 1
        obj.save()
        if data['drinks']:
            for d in data['drinks']:
                results.append({
            'id': d['idDrink'],
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
            'id': d['idDrink'],
            'name': d['strDrink'],
            'image': d['strDrinkThumb'],
        })


    return render(request, 'COCKTAIL/search.html', {'form': form, 'results': results})

def detail_page(request, id):
    results=[]
    url=f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}'

    response=requests.get(url)
    data=response.json()

    if data['drinks']:
        for d in data['drinks']:
            results.append({
                'name' : d['strDrink'],
                'image': d['strDrinkThumb'],
                'alcohol':d['strAlcoholic'],
                'instruction':d['strInstructions'],
                'ing1':d['strIngredient1'],
                'ing2':d['strIngredient2'],
                'ing3':d['strIngredient3'],
                'm1':d['strMeasure1'],
                'm2':d['strMeasure2'],
                'm3':d['strMeasure3'],
            })
    
    return render(request, 'COCKTAIL/display.html', {'results':results})

def show_result(request):
    drink=drink_model.objects.all().order_by('-drink_count')
    return render(request, "COCKTAIL/all_searches.html", {"drinks": drink})
