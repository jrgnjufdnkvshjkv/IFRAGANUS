from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArizaForm, KurslarForm, KonsultatsiyaForm
# Create your views here.

def index(request):
    ariza = ArizaForm(request.POST or None)

    if request.method == "POST" and ariza.is_valid():
        ariza.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
    "ariza": ariza
    }
    return render(request, 'index.html', context=context)


def kurslar(request):
    kurslar = KurslarForm(request.POST or None)
    if request.method == "POST" and kurslar.is_valid():
        kurslar.save()
        return HttpResponse("<h2>Sorovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
        "kurslar": kurslar
    }
    return render(request, 'index.html', context=context)


def konsultatsiya(request):
    konsultatsiya = KonsultatsiyaForm(request.POST or None)
    if request.method == "POST" and konsultatsiya.is_valid():
        konsultatsiya.save()
        return HttpResponse("<h2>Sorovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
        "konsultatsiya": konsultatsiya
    }
    return render(request, 'index.html', context=context)


