from django.shortcuts import render
# Create your views here.
def hello(request):
    return render(request,'hello.html')
def contact(request):
    return render(request,'contact.html')