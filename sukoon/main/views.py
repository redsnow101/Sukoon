from django.shortcuts import render,redirect
from django.http import HttpResponse


def landingPage(request):
    return HttpResponse("HEllo Sukkoon member")