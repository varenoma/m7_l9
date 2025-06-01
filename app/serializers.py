from rest_framework import serializers

from .models import ElectronLugatModel


class ElectronLugatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronLugatModel
        fields = ('uz_kiril', 'uz_lotin', 'tr', 'en', 'ru')


class ElectronLugatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronLugatModel
        fields = '__all__'
