from django.shortcuts import render , redirect ,HttpResponse 
from django.http import JsonResponse
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.views.generic import TemplateView
class SaveAppDetails(APIView) :
    def post(self , request) :
        serializer = Appserializer(data= request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response({"message" : "Data saved successfulley to the database","data" :serializer.data} , status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
class RetrieveData(APIView) :
    def get(self, request , pk) :
        try :
            app_detail = AppDetails.objects.get(id=pk)
            formated_data = {
                "app_name" : app_detail.app_name,
                "version" :  app_detail.version,
                "description" : app_detail.description
            }
            return Response({"message" : "Data retrieve successfull" ,"data" : formated_data},status=status.HTTP_202_ACCEPTED)
        except :
            return Response({"message" : f"App id {pk} doesnt exist.."},status=status.HTTP_404_NOT_FOUND)
class DeleteData(APIView) :
    def delete(self , request ,pk) :
        try:
            data_got = AppDetails.objects.get(id=pk)
            data_got.delete()
            return Response({"message":"Data removed successfully.."},status=status.HTTP_301_MOVED_PERMANENTLY)
        except :
            return Response({"message": f"The id {pk} doesnt exist"},status=status.HTTP_404_NOT_FOUND)
class MainView(TemplateView):
    template_name = 'index.html'


