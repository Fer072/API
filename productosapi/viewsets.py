from rest_framework import viewsets
from . import models
from . import serializers

class ProductoViewset(viewsets.ModelViewSet):
    queryset= models.Productos.objects.all()
    serializer_class=serializers.ProductoSerializer