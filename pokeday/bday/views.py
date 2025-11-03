from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def poke_day(request):
from django.shortcuts import render

def bday(request):
    return render(request, "poke_bday.html")