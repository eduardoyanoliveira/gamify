from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import  CustomUserSerialzier
from ..models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialzier
    
    def list(self, request, *args, **kwargs):      
        data = CustomUser.objects.filter(is_superuser=False)
        serializer = CustomUserSerialzier(data, many=True)
        return Response(serializer.data)
   
    def retrieve(self, request, *args, **kwargs):
        params = request.query_params

        if 'name' in params:
            data = CustomUser.objects.filter(username=params['name'])
            serializer = CustomUserSerialzier(data, many=True)
            return Response(serializer.data)