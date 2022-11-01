from rest_framework import serializers

from news.models import *


# ----------
# AboutService

class AboutServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutService
        fields = '__all__'


# ----------
# Features

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'


# ----------
# Features

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

# ----------
