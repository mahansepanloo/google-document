from django.shortcuts import render
from .models import DocumentModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import os
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import DocSerializers,CreateSerializers,CreateDocSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.http.response import HttpResponse
#????
from django.core.files import File
from django.core.files.base import ContentFile





class Showdoc(generics.ListAPIView):
    queryset = DocumentModel.objects.all()
    serializer_class = DocSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DocumentModel.objects.filter(user=self.request.user)

class UploudDoc(generics.CreateAPIView):
    queryset = DocumentModel.objects.all()
    serializer_class = CreateSerializers
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        creates = serializer.save(user=self.request.user)
        return creates


class Delete(generics.DestroyAPIView):
    queryset = DocumentModel.objects.all()
    serializer_class = DocSerializers
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            return super().perform_destroy(instance)
        else:
            raise PermissionDenied("You do not have permission to delete this document.")


class Download(APIView):
    def get(self, request, file):

        document = DocumentModel.objects.get(id=file)
        file_path = document.document.path
        file = open(file_path, 'r', encoding='utf-8')
        file_content = file.read()
        response = HttpResponse(file_content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{document.title or "document"}"'
        return response




class Create(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data =CreateDocSerializers(data=request.data)
        if data.is_valid():
            file_name = f"{data.validated_data.get('title', 'untitled')}"
            path_name = f"media/media/{file_name}"

            with open(path_name, 'r+') as file:
                document_instance = DocumentModel(
                    user=request.user,
                    title=data.validated_data.get('title','untitled'),
                    document = File(file, name=file_name)
                )
                document_instance.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)







class Update(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,file):
        objs = DocumentModel.objects.get(id=file)
        if objs.user == request.user:
            new_data = request.data
            path_name = f"media/media/{objs.title}.txt"
            with open(path_name,'w') as f:
                f.write(new_data['txt'])
            objs.document = File(open(path_name, 'rb'), name=objs.title)
            objs.save()
            return Response({'message': 'Document updated successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': '!!!!!!!!! updated successfully.'}, status=status.HTTP_200_OK)





