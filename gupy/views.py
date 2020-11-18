from django.shortcuts import render
from rest_framework import viewsets
from gupy.serializer import empresasSerializer, vagasSerializer
from gupy.models import empresas, vagas

# Create your views here.
class empresasViewSet(viewsets.ModelViewSet):
    
    queryset = empresas.objects.all()
    serializer_class = empresasSerializer

class vagasViewSet(viewsets.ModelViewSet):
    
    queryset = vagas.objects.all()
    serializer_class = vagasSerializer