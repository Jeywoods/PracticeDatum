from django.contrib.gis.db import models
from rest_framework import serializers

def validate_geometry(value):
    """
    Проверка валидности геометрии с использованием GEOS.
    """
    if not value.valid:
        raise serializers.ValidationError(value.valid_reason)

        
class Building(models.Model):
    
    """
    Модель строения, содержащая геометрию и адрес.
    Геометрия задаётся в формате WGS84 (EPSG:4326).
    """
    geom = models.GeometryField(srid=4326, validators=[validate_geometry])
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(type(self.geom)) + str(self.geom)