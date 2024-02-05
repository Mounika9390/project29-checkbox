from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):

    if request.method=='POST':
        tn=request.POST=['tn']
        NTO=Topic.objects.get_or_create(topic_name=tn)[0]
        NTO.save()
        return HttpResponse(tn)
    return render(request,'insert_topic.html')

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topic.html',d)

def insert_webpages(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        tn=request.POST=['tn']
        n=request.POST=['n']
        ur=request.POST=['ur']
        em=request.POST=['em']
        WO=Topic.objects.get(topic_name=tn)
        NWO=Webpage.objects.get_or_create(topic_name=WO,name=n,url=ur,email=em)[0]
        NWO.save()
        return HttpResponse('insert_webpages')
    return render(request,'insert_webpages.html',d)
def display_webpages(request):
    QLWO=Webpage.objects.all()
    d1={'webpage':QLWO}
    return render(request,'display_webpages.html',d1)

def insert_accessrecords(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        n=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']
        AO=Webpage.objects.get(name=n)
        NACO=AccessRecord.objects.get_or_create(name=AO,date=d,author=a)[0]
        NACO.save()
        return HttpResponse('insert_accessrecords')
    return render(request,'insert_accessrecords.html',d)
def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    d2={'accessrecod':QLAO}
    return render(request,'display_accessrecords.html',d2)

def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')#['C','FB','VB']
        #print(tn)
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)

        d1={'webpage':QLWO}
        return render(request,'display_webpages.html',d1) 

    return render(request,'select_multiple_webpage.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkbox.html',d)