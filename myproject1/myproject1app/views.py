from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from . models import Place
from . models import Team

def home(request):
    obj=Place.objects.all
    obj1 = Team.objects.all
    return render(request, "index.html", {'result':obj,'result1':obj1})




# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return render(request, "contact.html")
# def details(request):
#     return HttpResponse("our website details here")
# def close(request):
#     return HttpResponse("Thank you for visiting us")

# def operations(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res1 = x + y
#     res2 = x - y
#     res3 = x * y
#     res4 = x / y
#     return render(request, "result.html",
#                   {'add': res1, 'sub': res2, 'mul': res3, 'div': res4})
