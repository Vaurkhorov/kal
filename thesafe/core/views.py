from django.shortcuts import render

from recipes.models import Recipe, Ingredient
def index(request):

    return render(request, 'core/index.html')

def search(request, queryyy):
    recipe_list = Recipe.objects.filter(name__icontains=queryyy).values() # TO DO: add indices at the end later, check for 6.

    return render(
        request,
        "core/search.html"
        ,{
            "recipes": recipe_list
        }
        )

def alternative(request, queryname):
    recipe_list = Recipe.objects.filter(ingredient__isVegan=True).filter(name=queryname).values() # TO DO: add indices at the end later, check for 6.

    return render(
        request,
        "core/alternatives.html"
        ,{
            "recipes": recipe_list[0:1]
        }
        )

def about(request):
    return render(request, "core/about.html")

def favicon(request):
    return render(request, "https://vaurkhorov.github.io/make5/assets/faicon.ico")