from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .predication import model_predict
from .models import *


def user_logout(request):
    logout(request)
    return redirect("crops:login")


def user_registration(request):
    if request.user.is_authenticated:
        return redirect("crops:home")
    
    error = None
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                username=request.POST.get('email'),
                first_name = request.POST.get('fullname'),
                password=request.POST.get('password')
            )
            login(request, user)
            return redirect("crops:home")
        except:
            error = "User Already Exists"
    context = {
        "error": error
    }
    return render(request, "crops/registration.html", context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect("crops:home")
    
    error = None
    if request.method == "POST":
        try:
            user = get_object_or_404(User, username=request.POST.get("username"))
            if user.check_password(request.POST.get('password')):
                login(request, user)
                return redirect("crops:home")
            else:
                error = "Wrong User Password!"
        except:
            error = "User Does Not Exists!"
    
    context = {
        "error": error
    }
    return render(request, "crops/login.html", context)


@login_required(login_url="crops:login")
def home(request):
    result = False
    if request.method == "POST":
        crop_history = CropHistory.objects.create(
            nitrogen = request.POST.get("nitrogen"),
            phosphorus = request.POST.get("phosphorus"),
            potassium = request.POST.get("potassium"),
            temperature = request.POST.get("temperature"),
            humidity = request.POST.get("humidity"),
            ph_level = request.POST.get("ph"),
            rainfall = request.POST.get("rainfall"),
            user = request.user,
        )
        result = model_predict(request.POST.get("nitrogen"), request.POST.get("potassium"), request.POST.get("phosphorus"), request.POST.get("temperature"), request.POST.get("humidity"), request.POST.get("ph"), request.POST.get("rainfall"))
        crop_history.predication = result
        crop_history.save()
    
    context = {
        "result": result
    }
    return render(request, "crops/index.html", context)

