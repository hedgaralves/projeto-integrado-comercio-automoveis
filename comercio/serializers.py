from rest_framework import serializers
from .models import Cliente, Automovel, Venda

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class AutomovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovel
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
