from django.conf import settings
from rest_framework import serializers
import pytz
from .models import Movimentacao
from contas.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()
    def get_nome(self,obj):
        return f"{obj.first_name} {obj.last_name}"
    
    last_login = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S',default_timezone=pytz.timezone('America/Sao_Paulo'))
    class Meta:
        model = Usuario
        fields = [
            "id",
            "email",
            "nome",
            "last_login",
            "date_joined"
        ]

class MovimentacaoSerializer(serializers.ModelSerializer):
    deleted_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Movimentacao
        fields = "__all__"
        
class MovimentacaoSerializer2(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    
    class Meta:
        model = Movimentacao
        fields = [
            "id",
            "tipo",
            "valor",
            "data",
            "usuario"
        ]    