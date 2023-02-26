from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import index, search, about, favicon, alternative
from recipes.views import detail

urlpatterns = [
    path("", index, name = 'index'),
    path("favicon.ico", favicon, name = "favicon"),
    path("search/<str:queryyy>", search, name = "search"),
    path("about.html", about, name = "about"),
    path("alternatives/1/<str:queryname>", alternative, name = "alternatives"),
    path("recipe/<str:id>/", detail, name = "recipe"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)