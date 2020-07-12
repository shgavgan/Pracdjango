from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import modelform_factory
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from website.serializers import login1Serializer
from .models import *
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.core import serializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
"""
Class based function
"""

# class list(APIView):
#     def get(self,request):
#         log = login1.objects.all()
#         serializer=login1Serializer(log,many=True)
#         return Response(serializer.data)

@csrf_exempt
def list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        log = login1.objects.all()
        serializer = login1Serializer(log, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = login1Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sdetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sn = login1.objects.get(pk=pk)
    except sn.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = login1Serializer(sn)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = login1Serializer(sn, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sn.delete()
        return HttpResponse(status=204)



def index(request):
    return render(request,'website\index.html')

pform=modelform_factory(login1, exclude=[])
def login2(request):

    if request.method=='POST':
        form = pform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=pform()
    return render(request,"website\login.html",{"form":form})

