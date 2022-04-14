from animal.models import EspecieAnimal, LocalResgate, OrigemAnimal, MotivoResgate, RelatorioAnimal, Doador, FichaClinica, Alimentacao, Observacao, Ecdise, Morfometria, Animal
from animal.actions import animal_morto, imprimir_relatorio
# from animal.models import *

from django.contrib import admin



class LocalResgateAdmin(admin.ModelAdmin):
    list_display = (
        'municipio',
        'endereco',
        'area_resgate',
        'longitude',
        'latitude',
        )
    list_filter = (
        'municipio',
        'endereco',
        'area_resgate',
        )
    ordering = (
        'municipio',
        'endereco',
        'area_resgate',
        )
    search_fields = [
        'municipio', 
        'endereco', 
        'area_resgate',
        ]  
admin.site.register(LocalResgate, LocalResgateAdmin)

class OrigemAnimalAdmin(admin.ModelAdmin):
    list_display = (
        'descricao',
        )
    ordering = (
        'descricao',
        )
    search_fields = [
        'descricao'
        ]
admin.site.register(OrigemAnimal, OrigemAnimalAdmin)

class MotivoResgateAdmin(admin.ModelAdmin):
    list_display = (
        'descricao',
        )
    ordering = (
        'descricao',
        )
    search_fields = [
        'descricao'
        ]
admin.site.register(MotivoResgate, MotivoResgateAdmin)

class RelatorioAnimalAdmin(admin.ModelAdmin):
    list_display = (
        'local_resgate',
        'bo',
        'termo_destinacao',
        )
    list_filter = (
        'local_resgate__municipio',
        'local_resgate__endereco',
        'bo',
        'termo_destinacao',
        )
    ordering = (
        'local_resgate',
        'bo',
        'termo_destinacao',
        )
    search_fields = [
        'local_resgate', 
        'bo',
        'termo_destinacao',
        ]
admin.site.register(RelatorioAnimal, RelatorioAnimalAdmin)

class DoadorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'telefone',
        )
    list_filter = (
        'nome',
        'telefone',
        )
    ordering = (
        'nome',
        'telefone',
        )
    search_fields = [
        'nome', 
        'telefone',
        ]
admin.site.register(Doador, DoadorAdmin)

class EspecieAnimalAdmin(admin.ModelAdmin):
    list_display = (
        'nome_cientifico',
        'nome_popular',
        'classe',
        )
    list_filter = (
        'nome_cientifico',
        'nome_popular',
        'classe',
        )
    ordering = (
        'nome_cientifico',
        'nome_popular',
        'classe',
        )
    search_fields = [
        'nome_popular', 
        'classe', 
        'nome_cientifico',
        ]
admin.site.register(EspecieAnimal, EspecieAnimalAdmin)

class FichaClinicaInline(admin.StackedInline):
    model = FichaClinica
    extra = 1

class AlimentacaoInline(admin.StackedInline):
    model = Alimentacao
    extra = 1

class ObservacaoInline(admin.StackedInline):
    model = Observacao
    extra = 1

class EcdiseInline(admin.StackedInline):
    model = Ecdise
    extra = 1

class MorfometriaInline(admin.StackedInline):
    model = Morfometria
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    inlines = [
        AlimentacaoInline,
        FichaClinicaInline,
        ObservacaoInline,
        EcdiseInline,
        MorfometriaInline,
        ]
    autocomplete_fields = [
        'especie',
        'relatorio',
        'doador',
        ]
    list_display = (
        'especie',
        'codigo_interno',
        'data_entrada',
        'condicao_fisica',
        'esta_vivo',
        )
    list_filter = (
        'especie__classe',
        'especie__nome_popular',
        'especie__nome_cientifico',
        'codigo_interno',
        'data_entrada',
        'data_nascimento',
        'condicao_fisica',
        'esta_vivo',
        )
    ordering = (
        'especie',
        'codigo_interno',
        'data_entrada',
        'condicao_fisica',
        'esta_vivo',
        )
    actions = [
        animal_morto,
        imprimir_relatorio
        ]
admin.site.register(Animal, AnimalAdmin)
