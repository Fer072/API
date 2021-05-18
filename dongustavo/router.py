from productosapi.viewsets import ProductoViewset
from ventasapi.viewsets import VentaViewset
from rest_framework import routers, viewsets

router= routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('Venta', VentaViewset)