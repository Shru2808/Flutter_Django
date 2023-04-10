from rest_framework import serializers
from .models import candidates

class CanSerializer(serializers.ModelSerializer):
    class Meta:
        model = candidates
        fields = ['id','canname','email']