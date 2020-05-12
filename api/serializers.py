from rest_framework import serializers
from .models import Errand

#class that specifies what model (Errand) we want to serialize
class ErrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errand
        fields = '__all__'