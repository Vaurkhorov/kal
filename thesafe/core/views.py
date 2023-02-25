from django.shortcuts import render

from recipes.models import Recipe, Ingredient
def index(request):

    return render(request, 'core/index.html')

def search(request):
    recipe_list = Recipe.objects.filter(ingredient__hasGluten = True) # TO DO: add indices at the end later, check for 6.

    return render(
        request,
        "core/search.html"
        ,{
            "recipes": recipe_list
        }
        )

def about(request):
    return render(request, "core/about.html")