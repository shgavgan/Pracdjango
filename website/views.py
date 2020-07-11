from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import modelform_factory
# from website.models import login1
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from website.serializers import login1Serializer
from .models import *
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse


class list(APIView):
    def get(self,request):
        log = login1.objects.all()
        serializer=login1Serializer(log,many=True)
        return Response(serializer.data)


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


# task = {"summary": "Take out trash", "description": "" }
# resp = requests.post('https://todolist.example.com/tasks/', json=task)
# if resp.status_code != 201:
#     raise ApiError('POST /tasks/ {}'.format(resp.status_code))
# print('Created task. ID: {}'.format(resp.json()["id"]))