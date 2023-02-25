from django.contrib import admin
from django.urls import path

from core.views import index, recipe

urlpatterns = [
    path("", index, name = 'index'),
    path("Recipe.html", recipe, name = "recipe"),
    path('admin/', admin.site.urls),
]
