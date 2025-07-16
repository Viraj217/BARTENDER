from django import forms

class INGREDIENTFORM(forms.Form):
    ingredient = forms.CharField(label='Search by ingredient', max_length=100)

class DRINKFORM(forms.Form):
    drink = forms.CharField(label='Search for a drink', max_length=100)