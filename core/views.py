from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class Home(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')



def test(request):
    pass

