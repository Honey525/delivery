from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def customer_page(request):
    return render(request, 'index.html')

def courier_page(request):
    return render(request, 'index.html')