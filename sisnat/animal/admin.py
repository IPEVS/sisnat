from django.contrib import admin

from animal import actions, models, forms


@admin.register(models.Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'rua',
        'numero',
        'bairro',
        )
    ordering = (
        'rua',
        'numero',
        'bairro'
        )
    search_fields = [
        'rua',
        'numero',
        'bairro',
        'complemento'
        ]


@admin.register(models.LocalResgate)
class LocalResgateAdmin(admin.ModelAdmin):
    list_display = (
        'municipio',
        'endereco',
        'area_resgate',
        'longitude',
        'latitude',
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
    fieldsets = (
        ('Geral', {
            'fields': ('municipio', 'endereco', 'area_resgate')
        }), ('Posição', {
            'fields': ('longitude', 'latitude')
        }),
        )


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
    ordering = (
        'local_resgate',
        'bo',
        'termo_destinacao',
        )
    search_fields = [
        'local_resgate__municipio',
        'local_resgate__endereco',
        'bo',
        'termo_destinacao', 
        ]


@admin.register(models.Doador)
class DoadorAdmin(admin.ModelAdmin):
    list_display = (
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


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'data_saida',
        'observacao',
        )
    ordering = (
        'status',
        'data_saida',
        'observacao',
        )
    search_fields = [
        'status',
        'data_saida',
        'observacao',
        ]


@admin.register(models.EspecieAnimal)
class EspecieAnimalAdmin(admin.ModelAdmin):
    list_display = (
        'nome_cientifico',
        'nome_popular',
        'classe',
        )
    list_filter = (
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
    ordering = ['-criado_em']
    extra = 0


class AlimentacaoInline(admin.StackedInline):
    model = models.Alimentacao
    ordering = ['-criado_em']
    extra = 0


class ObservacaoInline(admin.StackedInline):
    model = models.Observacao
    ordering = ['-criado_em']
    extra = 0


class EcdiseInline(admin.StackedInline):
    form = forms.EcdiseForm
    model = models.Ecdise
    ordering = ['-criado_em']
    extra = 0


class MorfometriaInline(admin.StackedInline):
    form = forms.MorfometriaForm
    model = models.Morfometria
    ordering = ['-criado_em']
    extra = 0


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
        'status',
        )
    list_filter = (
        'especie__classe',
        'data_entrada',
        'condicao_fisica',
        'status__status',
        )
    ordering = (
        'especie',
        'codigo_interno',
        'data_entrada',
        'condicao_fisica',
        'status',
        )
    search_fields = [
        'especie__classe',
        'especie__nome_popular',
        'especie__nome_cientifico',
        'codigo_interno',
        'condicao_fisica',
        'status__status',
        ]
    actions = [
        actions.imprimir_relatorio,
        actions.export_excel
        ]