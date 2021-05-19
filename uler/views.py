from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Urls
import uuid,os
import socket

# Create your views here.
def index(request,url):
    try:
        init=Urls.objects.get(final=str(url))
        out=str(init.initial)

        return redirect(out)
    except:
        return HttpResponse("sorry,wrong url")

@api_view(['GET','POST'])
def shorter(request):
    if request.method=='POST':
        try:
            init = Urls.objects.get(initial=request.data['url'])
            new=init.final
            new=request.get_host()+"/"+new

        except:
            new=str(uuid.uuid4())[:5]
            init =Urls(initial=request.data['url'],final=new)
            init.save()
            new=request.get_host()+"/"+new
        out={"url":new}
        return Response({'data':out})
    return Response({'data':'NOT POST'})

@api_view(['GET','POST'])
def dels(request):
    message='not POST'
    if request.method=='POST':
        try:
            try:
                url=request.data['initial']
                db=Urls.objects.get(initial=url)
                db.delete()
            except:
                url=request.data['final']
                if url[:len(request.get_host())] ==request.get_host():
                    url=url[len(request.get_host())+1:]
                print(url)
                db=Urls.objects.get(final=url)
                db.delete()
            message="url was deleted"
        except:
            message="url does not exist or something goes wrong"
    return Response({'data':message})
