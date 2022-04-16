from django.contrib import admin

from animal import actions, models


@admin.register(models.LocalResgate)
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


@admin.register(models.OrigemAnimal)
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


@admin.register(models.MotivoResgate)
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


@admin.register(models.RelatorioAnimal)
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


@admin.register(models.Doador)
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


@admin.register(models.EspecieAnimal)
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


class FichaClinicaInline(admin.StackedInline):
    model = models.FichaClinica
    extra = 1


class AlimentacaoInline(admin.StackedInline):
    model = models.Alimentacao
    extra = 1


class ObservacaoInline(admin.StackedInline):
    model = models.Observacao
    extra = 1


class EcdiseInline(admin.StackedInline):
    model = models.Ecdise
    extra = 1


class MorfometriaInline(admin.StackedInline):
    model = models.Morfometria
    extra = 1


@admin.register(models.Animal)
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
        actions.animal_morto,
        actions.imprimir_relatorio
        ]
