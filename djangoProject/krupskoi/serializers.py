from rest_framework import fields, serializers
from djangoProject.krupskoi.models import Kalitka, Vorota

class VhodSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Kalitka
        fields = ("entry_code", "entry_name")

class VhodSerializer1(serializers.ModelSerializer):
    class Meta:
        model  = Vorota
        fields = ("entry_code", "entry_name")