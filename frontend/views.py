from django.shortcuts import render

# Create your views here.
def summary(request):
    return render(request, 'frontend/summary.html')

def about(request):
    return render(request, 'frontend/about.html')