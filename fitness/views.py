from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from health.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from health.forms import CustomUserCreationForm


def user_signup_form(request):
    if request.user.is_authenticated:
        return redirect('food_form')
    context = {}
    return render(request, 'authentication/signup.html', context)


def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_form')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'authentication/signup.html', context)


# def user_signup(request):
#     form = CustomUserCreationForm()
#     context = {}
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password_in_process = request.POST.get('password1')
#         cpassword_in_process = request.POST.get('password2')

#         if password_in_process != cpassword_in_process:
#             context['error'] = 'Password do not match'
#             return render(request, 'authentication/signup.html', context)
        
#         if form.is_valid():
#             form.save()
#             print('Umais')
#             return redirect('food_form')
#         else:
#             context['form'] = form
#     return render(request, 'authentication/signup.html', context)
        
    
    
def prevent_authenticated_access(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('food_form')  # Replace 'desired_url_name' with the desired URL
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def user_logout(request):
    logout(request)
    return redirect('user_login')

@prevent_authenticated_access
def user_login_form(request):
    context = {}
    return render(request, 'authentication/login.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('food_form')
        except:
            context['error'] = 'Username or password is invalid'
            context['username'] = username
            context['password'] = password
            return render(request, 'authentication/login.html', context)
    else:
        return redirect('user_login_form')
    
@login_required(login_url='user_login_form')
def food_form(request):
    context = {}
    food_instance_list = Food.objects.filter(user=request.user).order_by("-id")
    context['food_instance_list'] = food_instance_list
    try:
        if request.method == 'POST':
            date = request.POST.get('date')
            food_instance_list = Food.objects.filter(date_today=date, user=request.user)
            print(food_instance_list)
            context['food_instance_list'] = food_instance_list
    except:
        food_instance_list = Food.objects.filter(user=request.user).order_by("-id")
        context['food_instance_list'] = food_instance_list
    return render(request, 'health/templates/food.html', context)

def food(request):
    context = {}
    if request.method == 'POST':
        food = request.POST.get('food')
        calories = request.POST.get('calories')
        print(food, calories)
        user = User(id=request.user.id)
        food_instance = Food(food=food, calories=calories, user=user)
        food_instance.save()
        return redirect('food_form')
    else:
        return redirect('food_form')

@login_required(login_url='user_login_form')
def excercise_form(request):
    context = {}
    excercise_instance_raw = Excercise.objects.filter(user_refrence=request.user).order_by("-id")
    context['excercise_instance_raw'] = excercise_instance_raw
    try:
        if request.method == 'POST':
            date = request.POST.get('date')
            excercise_instance_raw = Excercise.objects.filter(date_today=date, user_refrence=request.user)
            context['excercise_instance_raw'] = excercise_instance_raw
    except:
        excercise_instance_raw = Excercise.objects.filter(user_refrence=request.user).order_by("-id")
        context['excercise_instance_raw'] = excercise_instance_raw
    return render(request, 'health/templates/excercise.html', context)

def excercise(request):
    context = {}
    if request.method == 'POST':
        excercise = request.POST.get('excercise')
        reps = request.POST.get('reps')
        user = User(id=request.user.id)
        excercise_instance = Excercise(excercise=excercise, reps=reps, user_refrence=user)
        excercise_instance.save()
        return redirect('excercise_form')
    else:
        return redirect('excercise_form')

@login_required(login_url='user_login_form')
def weight_form(request):
    context = {}
    weight_instance = Weight.objects.filter(user_refrence=request.user).order_by("-id")
    context['weight_instance'] = weight_instance
    try:
        if request.method == 'POST':
            date = request.POST.get('date')
            weight_instance = Weight.objects.filter(date_today=date, user_refrence=request.user)
            context['weight_instance'] = weight_instance
    except:
        weight_instance = Weight.objects.filter(user_refrence=request.user).order_by("-id")
        context['weight_instance'] = weight_instance

    return render(request, 'health/templates/weight.html', context)

def weight(request):
    context = {}
    if request.method == 'POST':
        weight = request.POST.get('weight')
        user = User(id=request.user.id)
        weight_instance = Weight(weight=weight, user_refrence=user)
        weight_instance.save()
        return redirect('weight_form')
    else:
        return redirect('weight_form')
    

# def search_food(request):
#     if request.method == 'POST':
#         date = request.POST.get('date')
#         food_filter_date = Food.objects.filter(date_today=date)
#         print(food_filter_date)
#         return redirect('food_form')