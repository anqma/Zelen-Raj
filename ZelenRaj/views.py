from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ZelenRaj.forms import PlantForm, OrderForm
from ZelenRaj.models import Plant


def order(request):
    if request.method == "POST":
        form_data = PlantForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            o = form_data.save(commit=False)
            o.user = request.user
            o.save()
            return redirect("thankYou")
    context = {"form": OrderForm}
    return render(request, "order.html", context)


def homepage(request):
    return render(request, "homepage.html")


def mycart(request):
    return render(request, "mycart.html")


@login_required
def addPlant(request):
    if not request.user.is_superuser:
        return HttpResponse(
            "Не можете да додадете растение. Само администраторите(продавачи) имаат овластување за тоа.")

    if request.method == "POST":
        form_data = PlantForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            plant = form_data.save(commit=False)
            plant.user = request.user
            plant.image = form_data.cleaned_data['image']
            plant.save()
            return redirect("plants")
    else:
        form_data = PlantForm()

    context = {"form": form_data}
    return render(request, "addPlant.html", context)


def plants(request):
    queryset = Plant.objects.all()
    context = {"plants": queryset}
    return render(request, "plants.html", context)


def selectedPlant(request, name):
    plant = Plant.objects.get(name=name)
    context = {"plant": plant}
    return render(request, "selectedPlant.html", context)


def thankYou(request):
    return render(request, "thankYou.html")
