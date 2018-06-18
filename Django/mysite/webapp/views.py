from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>Hey there, Soham here with his first app</h2>")
# Create your views here.
