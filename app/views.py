from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,JsonResponse
from num2words import num2words
from gtts import gTTS
from playsound import playsound

# Create your views here.

def index(request):
    ab=speaker(id=1,lid=1,speak="song.mp3",num=0)
    ab.save()
    for i in range(1,11):
        ab=mult(lid=i,count=0)
        ab.save()
    return render(request,"index.html",{})
def redirect(request):
    return render(request,"index.html",{})
def multiplier(request):
    if request.method=="POST":
        num=request.POST.get("num")
        if(num==""):
            return HttpResponse("<script>alert('Enter a number');window.location.href='/redirect/';</script>")
        txt=""
        text=""
        for i in range(1,11):
            mul=i*int(num)
            val=num2words(num)
            txt=str(i)+" "+str(val)+"'s"+" "+"are"+" "+str(mul)+("\n")+("\n")
            text+=str(i)+" "+str(val)+"'s"+" "+"are"+" "+str(mul)+("\n")+("\n")
            ab=mult.objects.get(lid=i)
            ab.count=txt
            ab.save()
        ab=speaker.objects.get(id=1,lid=1)
        ob=gTTS(text)
        ab.speak=ob.save("song.mp3")
        ab.num=1
        ab.save()
        ab=mult.objects.all()
        return render(request,"index.html",{"data":ab})
def audio(request):
    ab=speaker.objects.get(lid=1)
    if(ab.num==0):
        return HttpResponse("<script>alert('Please enter a number and submit it');window.location.href='/redirect/';</script>")
    playsound("song.mp3")
    ab.lid=1
    ab.speak="song.mp3"
    ab.num=0
    ab.save()
    return render(request,"index.html",{})
