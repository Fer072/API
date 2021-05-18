from rest_framework import viewsets
from . import models
from . import serializers

class VentaViewset(viewsets.ModelViewSet):
    queryset= models.Venta.objects.all()
    serializer_class=serializers.VentaSerializer