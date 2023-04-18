from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def Naveen(request):
    STD=studentinfo()
    d={"ST":STD}
    if request.method=='POST':
        N=studentinfo(request.POST)
        if N.is_valid():
            return HttpResponse(str(N.cleaned_data))


    return render(request,'Naveen.html',d)