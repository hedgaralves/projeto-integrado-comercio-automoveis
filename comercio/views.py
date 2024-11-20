from rest_framework import viewsets
from .models import Cliente, Automovel, Venda
from .serializers import ClienteSerializer, AutomovelSerializer, VendaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class AutomovelViewSet(viewsets.ModelViewSet):
    queryset = Automovel.objects.all()
    serializer_class = AutomovelSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
