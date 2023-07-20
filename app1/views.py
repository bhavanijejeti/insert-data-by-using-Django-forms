from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def djforms(request):
    sufo=signupforms()
    d={'sufo':sufo}
    if request.method=='POST':
        sufdt=signupforms(request.POST)
        if sufdt.is_valid():
            name=sufdt.cleaned_data['name']
            return HttpResponse(str(sufdt.cleaned_data))
    return render(request,'djforms.html',d)

def insertwebpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
    return render(request,'insertwebpage.html',d)


