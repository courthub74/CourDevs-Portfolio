from django.shortcuts import render

#HomePage
def home(request):
    return render(request, "home.html", {})
