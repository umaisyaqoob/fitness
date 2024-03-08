"""
URL configuration for fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls import static
from django.conf import settings
from fitness import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup-form/', views.user_signup_form, name='user_signup_form'),
    path('login-form/', views.user_login_form, name='user_login_form'),
    path('', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('food-form/', views.food_form, name='food_form'),
    path('excercise-form/', views.excercise_form, name='excercise_form'),
    path('weight-form/', views.weight_form, name='weight_form'),
    path('food/', views.food, name='food'),
    path('excercise/', views.excercise, name='excercise'),
    path('weight/', views.weight, name='weight'),
    path('logout/', views.user_logout, name='user_logout'),
    # path('search-food/', views.search_food, name='search_food'),
]


if settings.DEBUG == 'True':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)