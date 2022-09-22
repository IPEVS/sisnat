from django import forms
from django.db import models
from django.forms import ValidationError

from core.models import BaseModel
from animal import choices


class EspecieAnimal(BaseModel):
    classe = models.CharField(
        max_length=9,
        choices=choices.CLASSE_ANIMAIS_CHOICES,
        verbose_name='Classe do animal',
        )
    nome_cientifico = models.CharField(
        max_length=100,
        verbose_name='Nome Científico',
        )
    nome_popular = models.CharField(
        max_length=100,
        verbose_name='Nome Popular',
        )

    class Meta:
        verbose_name = 'Especie do Animal'
        verbose_name_plural = 'Especie dos Animais'

    def __str__(self):
        return (f"{self.classe} | "
                f"{self.nome_cientifico} | "
                f"{self.nome_popular}")


class Endereco(BaseModel):
    rua = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Rua',
        )
    numero = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name='Número',
        )
    complemento = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Complemento',
        )
    bairro = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Bairro',
        )
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereço'

    def __str__(self):
        return (f"{self.rua} n: "
                f"{self.numero}")


class LocalResgate(BaseModel):
    municipio = models.CharField(
        verbose_name='Município de origem',
        max_length=50,
        )
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        verbose_name='Endereço',
        blank=True,
        null=True,
        )
    area_resgate = models.CharField(
        verbose_name='Área do resgate',
        choices=choices.AREA_RESGATE_CHOICES,
        default=choices.AREA_R,
        max_length=15,
        )
    longitude = models.FloatField(
        max_length=12,
        blank=True,
        null=True,
        verbose_name='Longitude',
        )
    latitude = models.FloatField(
        max_length=12,
        blank=True,
        null=True,
        verbose_name='Latitude',
        )

    def __str__(self):
        return (f"Município: {self.municipio} \n"
                f"Endereço: {self.endereco} \n")

    class Meta:
        verbose_name = 'Local do Resgate'
        verbose_name_plural = 'Locais do Resgate'


class OrigemAnimal(BaseModel):
    descricao = models.CharField(
        max_length=50,
        verbose_name='Descrição',
        )

    def __str__(self):
        return (f"{self.descricao} \n")

    class Meta:
        verbose_name = 'Origem'
        verbose_name_plural = 'Origem'


class MotivoResgate(BaseModel):
    descricao = models.CharField(
        max_length=80,
        verbose_name='Descrição',
        )

    def __str__(self):
        return (f"{self.descricao} \n")

    class Meta:
        verbose_name = 'Motivo'
        verbose_name_plural = 'Motivos'


class RelatorioAnimal(BaseModel):
    local_resgate = models.ForeignKey(
        LocalResgate,
        on_delete=models.RESTRICT,
        verbose_name='Local de Resgate',
        )
    bo = models.CharField(
        verbose_name='Boletim de ocorrência',
        max_length=50,
        blank=True,
        null=True,
        )
    termo_destinacao = models.CharField(
        verbose_name='Termo de destinação',
        max_length=50,
        blank=True,
        null=True,
        )
    origem = models.ForeignKey(
        OrigemAnimal,
        on_delete=models.SET_NULL,
        verbose_name='Origem',
        blank=True,
        null=True,
        )
    motivo = models.ForeignKey(
        MotivoResgate,
        on_delete=models.SET_NULL,
        verbose_name='Motivo do resgate',
        blank=True,
        null=True,
        )
    observacao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observação',
        )
    def __str__(self):
        return (f"Local Resgate: {self.local_resgate} \n")
    class Meta:
        verbose_name = 'Resgate'
        verbose_name_plural = 'Resgate'


class Doador(BaseModel):
    nome = models.CharField(
        verbose_name='Nome do doador',
        max_length=50,
        blank=True,
        null=True,
        )
    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Telefone',
        )
    def __str__(self):
        return (f"Nome doador: {self.nome} \n")
    class Meta:
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'


class Status(BaseModel):
    status = models.CharField(
        max_length=50,
        verbose_name='Status',
        choices=choices.STATUS_CHOICES,
        default=choices.P_IPEVS,
        )
    data_saida = models.DateField(
        verbose_name='Data de Saída',
        blank=True,
        null=True,
        )
    observacao = models.TextField(
        verbose_name='Observação',
        blank=True,
        null=True,
        )

    def __str__(self):
        return (f"{self.status} \n")

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Animal(BaseModel):
    especie = models.ForeignKey(
        EspecieAnimal,
        on_delete=models.RESTRICT,
        verbose_name='Animal',
        )
    # imagem = models.ImageField(
    #     blank=True,
    #     null=True,
    #     upload_to='images/',
    #     )
    codigo_interno = models.CharField(
        max_length=30,
        verbose_name='Código Interno',
        unique=True,
        )
    data_entrada = models.DateField(
        verbose_name='Data de entrada',
        )
    data_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        blank=True,
        null=True,
        )
    sexo = models.CharField(
        max_length=10,
        choices=choices.SEXO_CHOICES,
        default=choices.INDEFINIDO,
        verbose_name='Sexo',
        )
    faixa_etaria = models.CharField(
        verbose_name='Faixa etária',
        max_length=7,
        choices=choices.FAIXA_ETARIA_CHOICES,
        )
    condicao_fisica = models.CharField(
        verbose_name='Condição Física',
        max_length=7,
        choices=choices.CONDICAO_FISICA_CHOICES,
        default=choices.BOA,
        )
    # esta_vivo = models.BooleanField(
    #     default=True,
    #     verbose_name='O animal está vivo?',
    #     )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name='Status',
        )
    relatorio = models.ForeignKey(
        RelatorioAnimal,
        on_delete=models.RESTRICT,
        verbose_name='Relatório',
        )
    doador = models.ForeignKey(
        Doador,
        on_delete=models.SET_NULL,
        verbose_name='Doador',
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return (f"{self.especie.nome_popular}"
                f" Cod: {self.codigo_interno}")


class FichaClinica(BaseModel):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        )
    data_procedimento = models.DateField(
        verbose_name='Data da observação',
        )
    procedimento = models.TextField(
        blank=True,
        null=True,
        verbose_name='Procedimento',
        )

    class Meta:
        verbose_name = 'Ficha Clínica'
        verbose_name_plural = 'Fichas Clínicas'


class Alimentacao(BaseModel):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        )
    data_alimentacao = models.DateField(
        verbose_name='Data da alimentação',
        )
    alimento = models.CharField(
        max_length=200,
        verbose_name='Alimento'
        )
    unidade_de_medida = models.CharField(
        verbose_name='Unidade de medida',
        choices=choices.UNIDADE_DE_MEDIDA_CHOICES,
        default=choices.GRAMAS,
        max_length=7,
        blank=True,
        null=True,
        )
    quantidade = models.FloatField(
        blank=True,
        null=True,
        )
    sobra = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name = 'Alimentação'
        verbose_name_plural = 'Alimentações'


class Observacao(BaseModel):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        )
    data_observacao = models.DateField(
        verbose_name='Data da observação',
        )
    observacao = models.TextField(
        verbose_name='Observação',
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name = 'Observação'
        verbose_name_plural = 'Observações'


class Ecdise(BaseModel):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        )
    classe = models.CharField(
        max_length=9,
        choices=choices.CLASSE_ANIMAIS_CHOICES,
        verbose_name='Classe do animal',
        )
    data_ecdise = models.DateField(
        verbose_name='Data da ecdise',
        )
    ecdise = models.CharField(
        max_length=10,
        choices=choices.ECDISE_CHOICES,
        default=choices.INCOMPLETA,
    )
    # imagem_ecdise = models.ImageField(
    #     blank=True,
    #     null=True,
    #     upload_to='images/ecdise/amphibia/',
    #     )

    class Meta:
        verbose_name = 'Ecdise'
        verbose_name_plural = 'Ecdise'


class Morfometria(BaseModel):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        )
    classe = models.CharField(
        max_length=9,
        choices=choices.CLASSE_ANIMAIS_CHOICES,
        verbose_name='Classe do animal',
        )
    data_medicao = models.DateField(
        verbose_name='Data da medição',
        )
    peso = models.CharField(
        verbose_name='Peso',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_corpo = models.CharField(
        verbose_name='Comprimento corpo',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_pernas = models.CharField(
        verbose_name='Comprimento pernas',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_pedipalpos = models.CharField(
        verbose_name='Comprimento pedipalpos',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_calda = models.CharField(
        verbose_name='Comprimento da calda',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_femur = models.CharField(
        verbose_name='Comprimento fêmur',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_cabeca = models.CharField(
        verbose_name='Comprimento cabeça',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_rosto_cloacal = models.CharField(
        verbose_name='Comprimento rostro-cloacal',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_tibia = models.CharField(
        verbose_name='Comprimento tíbia',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_tarso = models.CharField(
        verbose_name='Comprimento do tarso',
        max_length=10,
        blank=True,
        null=True,
        )
    dist_olho_narina = models.CharField(
        verbose_name='Distância entre olho-narina',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_asa = models.CharField(
        verbose_name='Comprimento da asa',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_bico = models.CharField(
        verbose_name='Comprimento do bico',
        max_length=10,
        blank=True,
        null=True,
        )
    altura_bico = models.CharField(
        verbose_name='Altura do bico',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_pe = models.CharField(
        verbose_name='Comprimento do pé',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_mao = models.CharField(
        verbose_name='Comprimento da mão',
        max_length=10,
        blank=True,
        null=True,
        )
    comp_rosto_anal = models.CharField(
        verbose_name='Comprimento rostro-anal',
        max_length=10,
        blank=True,
        null=True,
        )
    altura_orelha = models.CharField(
        verbose_name='Altura da orelha',
        max_length=10,
        blank=True,
        null=True,
        )
    observacao = models.TextField(
        verbose_name='Observação',
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name = 'Morfometria'
        verbose_name_plural = 'Morfometria'