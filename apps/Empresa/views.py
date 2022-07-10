from django.shortcuts import render
from .serializers import SedeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sede 
# Create your views here.

class SedeAPI(APIView):
    def get_queryset(self,pk):
        try:
            return Sede.objects.get(id=pk)
        except Sede.DoesNotExist:
            raise Http404


    def get(self,request,format=None):
        queryset = Sede.objects.all()
        serializer=SedeSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = SedeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request,pk,format=None):
        obj = self.get_queryset(pk)
        serializer = SedeSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        obj = self.get_queryset(pk)
        if obj:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)