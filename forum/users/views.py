from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name="test.html",context={'first_name': 'John', 'last_name': 'Doe'})