"""lafleur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-sections/', views.GetList),
    path('all-sections/bouquets/', views.GetBouquets, name='bouquets_url'),
    path('all-sections/plants/', views.GetPlants, name='plants_url'),
    path('all-sections/flowers/', views.GetFlowers, name='flowers_url'),
    path('all-sections/reasons/', views.GetReasons, name='reasons_url'),
    path('all-sections/reasons/birthday/', views.GetBirthday, name='birthday_url'),
    path('all-sections/reasons/wedding/', views.GetWedding, name='wedding_url')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
