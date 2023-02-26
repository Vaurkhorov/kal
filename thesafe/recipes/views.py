from django.shortcuts import render, get_object_or_404
from .models import Recipe

def detail(request, id):
    recipe = Recipe.objects.filter(name = id).values()[0]

    return render(request, "recipe/recipe.html/", {
        "recipe": recipe,
    })