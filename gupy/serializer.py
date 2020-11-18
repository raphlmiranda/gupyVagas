from rest_framework import serializers
from gupy.models import empresas, vagas

class empresasSerializer(serializers.ModelSerializer):

    class Meta:
        model = empresas
        fields = ['id', 'name', 'status']

class vagasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = vagas
        fields = ['id', 'name', 'depart', 'link', 'data', 'id_empresa']

