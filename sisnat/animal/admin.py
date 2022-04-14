from django.contrib import admin
from django.shortcuts import render, redirect, HttpResponse
   
from animal.models import *

class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = []

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
    search_fields = []

admin.site.register(EspecieAnimal, EspecieAnimalAdmin)


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
        # 'longitude',
        # 'latitude',
        )
    ordering = (
        'municipio',
        'endereco',
        'area_resgate',
        # 'longitude',
        # 'latitude',
        )   

admin.site.register(LocalResgate, LocalResgateAdmin)


class OrigemAnimalAdmin(admin.ModelAdmin):
    list_display = (
        'descricao',
        )
    # list_filter = (
    #     'descricao',
    #     )
    ordering = (
        'descricao',
        )

admin.site.register(OrigemAnimal, OrigemAnimalAdmin)


class MotivoResgateAdmin(admin.ModelAdmin):
    list_display = (
        'descricao',
        )
    # list_filter = (
    #     'descricao',
    #     )
    ordering = (
        'descricao',
        )

admin.site.register(MotivoResgate, MotivoResgateAdmin)


class RelatorioAnimalAdmin(admin.ModelAdmin):
    list_display = (
        'local_resgate',
        'bo',
        'termo_destinacao',
        # 'origem',
        # 'motivo',
        # 'soltura',
        )
    list_filter = (
        'local_resgate__municipio',
        'local_resgate__endereco',
        # 'local_resgate__area_resgate',
        # 'local_resgate__longitude',
        # 'local_resgate__latitude',
        'bo',
        'termo_destinacao',
        # 'origem__descricao',
        # 'motivo__descricao',
        # 'soltura',
        )
    ordering = (
        'local_resgate',
        'bo',
        'termo_destinacao',
        # 'origem',
        # 'motivo',
        # 'soltura',
        )

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

admin.site.register(Doador, DoadorAdmin)


class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'especie',
        # 'imagem_animal',
        'codigo_interno',
        'data_entrada',
        # 'data_nascimento',
        # 'sexo',
        # 'faixa_etaria',
        'condicao_fisica',
        'esta_vivo',
        # 'relatorio',
        # 'doador',
        )
    list_filter = (
        'especie__classe',
        'especie__nome_popular',
        'especie__nome_cientifico',
        'codigo_interno',
        'data_entrada',
        'data_nascimento',
        # 'sexo',
        # 'faixa_etaria',
        'condicao_fisica',
        'esta_vivo',
        # 'relatorio',
        # 'doador',
        )
    ordering = (
        'especie',
        # 'imagem_animal',
        'codigo_interno',
        'data_entrada',
        # 'data_nascimento',
        # 'sexo',
        # 'faixa_etaria',
        'condicao_fisica',
        'esta_vivo',
        # 'relatorio',
        # 'doador',
        )
    actions = [

        ]

admin.site.register(Animal, AnimalAdmin)


class FichaClinicaAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'data_procedimento',
        # 'procedimento',
        )
    list_filter = (
        'animal__codigo_interno',
        'animal__data_entrada',
        'data_procedimento',
        # 'procedimento',
        ) 
    ordering = (
        'animal',
        'data_procedimento',
        # 'procedimento',
        )  

admin.site.register(FichaClinica, FichaClinicaAdmin)


class AlimentacaoAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'data_alimentacao',
        )
    list_filter = (
        'animal__codigo_interno',
        'animal__data_entrada',
        'data_alimentacao',
        # 'alimento',
        # 'quantidade',
        # 'sobra',
        )
    ordering = (
        'animal',
        'data_alimentacao',
        # 'procedimento',
        )  

admin.site.register(Alimentacao, AlimentacaoAdmin)


class ObservacaoAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'data_observacao',
        )
    list_filter = (
        'animal__codigo_interno',
        'animal__data_entrada',
        'data_observacao',
        )
    ordering = (
        'animal',
        'data_observacao',
        # 'procedimento',
        ) 

admin.site.register(Observacao, ObservacaoAdmin)


class EcdiseAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'classe',  
        'data_ecdise',
        'ecdise',
        # 'imagem_ecdise',
        )
    list_filter = (
        'animal__codigo_interno',
        'animal__data_entrada',
        'classe',
        'data_ecdise',
        'ecdise',
        )
    ordering = (
        'animal', 
        'classe', 
        'data_ecdise',
        'ecdise',
        )

admin.site.register(Ecdise, EcdiseAdmin)


class MorfometriaAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'classe',
        'data_medicao',
        )
    list_filter = (
        'animal__codigo_interno',
        'animal__data_entrada',
        'classe',
        'data_medicao',
        # 'cc',
        # 'cf',
        # 'cp',
        # 'cpp',
        # 'crc',
        # 'ct',
        # 'cta',
        # 'don',
        # 'peso',
        # 'ca',
        # 'cb',
        # 'h',
        # 'cm',
        # 'cra',
        # 'ho',
        # 'observacao',
        )
    ordering = (
        'animal',
        'classe',
        'data_medicao',
        )

admin.site.register(Morfometria, MorfometriaAdmin)