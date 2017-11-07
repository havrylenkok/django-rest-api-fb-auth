from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Place
        fields = ('id', 'name', 'date_created', 'date_modified', 'long_position', 'lat_position', 'avatar_url')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_superuser', 'username')


