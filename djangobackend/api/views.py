from django.shortcuts import render

from .models import candidates
from .serializers import CanSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class CanList(ListAPIView):
    queryset = candidates.objects.all()
    serializer_class = CanSerializer