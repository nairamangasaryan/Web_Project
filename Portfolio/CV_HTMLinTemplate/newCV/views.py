from django.shortcuts import render

# Create your views here.

def newCV(request):
    return render(request, "newCV.html")
