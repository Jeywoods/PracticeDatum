from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers
from .models import Building


class BuildingSerializer(geo_serializers.GeoFeatureModelSerializer):
    """
    Сериализатор для модели Building в формате GeoJSON (Feature).
    Позволяет передавать и получать геоданные через API.
    """
    class Meta:
        model = Building
        geo_field = 'geom'
        fields = ['id', 'geom', 'address']
        read_only_fields = ['id']