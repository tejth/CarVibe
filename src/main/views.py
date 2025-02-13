from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from main.models import Listing
# Create your views here.

def main_view(request):
    return render(request, "views/main.html",{"name":"CarVibe"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
         'listings': listings,
    }
    return render(request,"views/home.html", context)


@login_required
def list_view(request):
    if request.method=='POST':
        pass
    elif request.method =='GET':
        pass
    return render(request , 'views/list.html',{})

