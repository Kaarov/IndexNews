from rest_framework import serializers

from news.models import *


# ----------
# AboutService

class AboutServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutService
        fields = '__all__'


# ----------
# Slogan / Slogan Items

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
# AboutUs / About Us Items

class AboutUsItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsItems
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    about_us_items = serializers.SerializerMethodField('get_about_us_items')

    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description', 'image', 'active', 'created', 'about_us_items']

    def get_about_us_items(self, obj):
        about_us_items = AboutUsItems.objects.filter(about_us=obj)
        return AboutUsItemsSerializer(about_us_items, many=True).data


# ----------
# Services / Services Items

class ServicesItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesItems
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    services_items = serializers.SerializerMethodField('get_services_items')

    class Meta:
        model = Services
        fields = ['id', 'title', 'image', 'active', 'created', 'services_items']

    def get_services_items(self, obj):
        services_items = ServicesItems.objects.filter(services=obj)
        return ServicesItemsSerializer(services_items, many=True).data


# ----------
# Features

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'


# ----------
# Partners

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


# ----------
# News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


# ----------
# Contacts

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

# ----------
