from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')  

def terms_and_conditions(request):
    return render(request, 'website/terms.html')  

def about(request):
    return render(request, 'website/about.html')