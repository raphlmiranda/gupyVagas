from django.contrib import admin
from gupy.models import empresas, vagas

# Register your models here.
class Empresas(admin.ModelAdmin):
    '''
    Empresas CRUD
    '''
    list_display = ('id', 'name', 'status')
    search_fields = ('name','status',)
    list_per_page = 100

admin.site.register(empresas, Empresas)

class Vagas(admin.ModelAdmin):
    '''
    Vagas CRUD
    '''
    list_display = ('id', 'name', 'depart', 'data', 'id_empresa', 'link')
    search_fields = ('name',)
    list_per_page = 100

admin.site.register(vagas, Vagas)