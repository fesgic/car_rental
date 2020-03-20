from django.contrib import admin
from django.urls import path
from . import views as rental_views
from django.contrib.auth import views as auth_views

urlpatterns=[
path('',rental_views.home,name='rental_app-home'),
path('rentals/',rental_views.rentals,name='rental_app-rentals'),
#path('login/',auth_views.LoginView.as_view(template_name='rental_app/home.html'),)
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)