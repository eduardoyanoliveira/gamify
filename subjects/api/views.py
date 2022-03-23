from rest_framework import viewsets
from ..models import Subject, Content, Keyword
from .serializers import  SubjectSerializer, ContentSerializer, KeywordSerializer

# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.filter(is_active=True)
    serializer_class = SubjectSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.filter(is_active=True)
    serializer_class = ContentSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer