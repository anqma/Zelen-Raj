"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ZelenRaj.views import homepage, mycart, plants, thankYou, selectedPlant, order, addPlant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', order, name="order"),
    path('homepage/', homepage, name="homepage"),
    path('mycart/', mycart, name="mycart"),
    path('plants/', plants, name="plants"),
    path('addPlant/', addPlant, name="addPlant"),
    path('plants/<str:name>/', selectedPlant, name="selectedPlant"),
    path('thankYou/', thankYou, name="thankYou"),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
