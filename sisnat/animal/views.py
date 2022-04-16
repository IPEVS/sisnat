from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request, 'animal/home_page.html')

@login_required(login_url='/sisnat/')
def pdf_page(request):
    return render(request, 'animal/pdf_page.html')