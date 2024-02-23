from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def agent(request):
    return render(request,'agent-single.html')

def agents(request):
    return render(request,'agents-grid.html')

def blogg(request):
    return render(request,'blog-grid.html')

def blogs(request):
    return render(request,'blog-single.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def propertyg(request):
    return render(request,'property-grid.html')

def propertys(request):
    return render(request,'property-single.html')

