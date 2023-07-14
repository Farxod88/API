from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TalabaSerializers
from .models import *



# Create your views here.
@api_view(['GET','POST'])
def Test(request):
    tex = Talaba.objects.all()
    serializer = TalabaSerializers(tex, many=True)
    return Response({'status':200,'data':serializer.data})


@api_view(['GET','POST'])
def Test_post(request):
    data = request.data
    serializer = TalabaSerializers(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403, 'xatolik':serializer.errors,'message':'xatolik yuz berdi!'})
    serializer.save()
    
    return Response({'status':200, 'data':serializer.data, 'message':'malumot qabul qilindi!'})
