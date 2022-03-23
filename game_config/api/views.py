from rest_framework import viewsets
from ..models import UserLevel, Difficulty
from .serializers import UserLevelSerializer, DifficultySerializer

# Create your views here.
class UserLevelViewSet(viewsets.ModelViewSet):
    queryset = UserLevel.objects.all()
    serializer_class = UserLevelSerializer


class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer