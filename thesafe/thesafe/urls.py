from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import index, search, about
from recipes.views import detail

urlpatterns = [
    path("", index, name = 'index'),
    path("search.html", search, name = "search"),
    path("about.html", about, name = "about"),
    path("recipe/<str:id>/", detail, name = "recipe"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)