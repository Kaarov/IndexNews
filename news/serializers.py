from rest_framework import serializers

from news.models import *


# ----------
# AboutService

class AboutServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutService
        fields = '__all__'


# ----------
# Slogan

class SloganItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SloganItems
        fields = '__all__'


class SloganSerializer(serializers.ModelSerializer):
    slogan_items = serializers.SerializerMethodField('get_slogan_items')

    class Meta:
        model = Slogan
        fields = ['id', 'title', 'description', 'active', 'created', 'slogan_items']

    def get_slogan_items(self, obj):
        slogan_items = SloganItems.objects.filter(slogan=obj)
        return SloganItemsSerializer(slogan_items, many=True).data


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
