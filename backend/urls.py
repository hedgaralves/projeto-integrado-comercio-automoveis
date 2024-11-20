from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comercio.views import ClienteViewSet, AutomovelViewSet, VendaViewSet

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('automoveis', AutomovelViewSet)
router.register('vendas', VendaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
