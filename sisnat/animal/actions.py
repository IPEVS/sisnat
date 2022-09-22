from datetime import datetime
from tkinter import commondialog
import io

from django import http
from django.shortcuts import render
from django.contrib import admin
from pytz import timezone
import pandas as pd
import numpy as np
import xlwt
import openpyxl

from core import utils
from animal import models


@admin.action(description="Trocar animais selecionados para morto")
def animal_morto(modeladmin, request, queryset):
    queryset.update(esta_vivo=False)


@admin.action(description="Relatório dos selecionados")
def imprimir_relatorio(self, request, queryset):
    animals = []
    for animal in queryset:
        animal_data = animal.__dict__
        # animal_data.pop('_state')  # django_internal_key

        # TODO: parse datetimes to BR tz: `criado_em` and `atualizado_em`
        animal_data['especie'] = animal.especie.__dict__

        # Relatorio
        relatorio = animal.relatorio
        animal_data['relatorio'] = relatorio.__dict__
        animal_data['relatorio']['local_resgate'] = relatorio.local_resgate.__dict__
        relatorio_fks = ['origem', 'motivo']
        for relatorio_fk in relatorio_fks:
            obj = getattr(relatorio, relatorio_fk, None)
            if obj is not None:
                animal_data['relatorio'][relatorio_fk] = obj.__dict__
        animal_data['relatorio']['local_resgate']['endereco'] = relatorio.local_resgate.endereco.__dict__

        # Status
        if animal.status is not None:
            animal_data['status'] = animal.status.__dict__
        
        # Doador
        if animal.doador is not None:
            animal_data['doador'] = animal.doador.__dict__

        # FichaClinica
        fichas = []
        for ficha in animal.fichaclinica_set.all():
            fichas.append(ficha.__dict__)
        animal_data['fichas_clinicas'] = fichas

        # Alimentacao
        alimentos = []
        for alimento in animal.alimentacao_set.all():
            alimentos.append(alimento.__dict__)
        animal_data['alimentacao'] = alimentos

        # Observacao
        observacoes = []
        for observacao in animal.observacao_set.all():
            observacoes.append(observacao.__dict__)
        animal_data['observacoes'] = observacoes

        # Ecdise
        ecdises = []
        for ecdise in animal.ecdise_set.all():
            ecdises.append(ecdise.__dict__)
        animal_data['ecdises'] = ecdises

        # Morfometria
        morfometrias = []
        for morfometria in animal.morfometria_set.all():
            morfometrias.append(morfometria.__dict__)
        animal_data['morfometrias'] = morfometrias

        animals.append(animal_data)

    now = datetime.now(tz=timezone('America/Sao_Paulo'))
    now_formatted = utils.format_datetime_to_brt(now)
    context = {'animals': animals, 'generated_at': now_formatted}
    return render(
            request,
            'animal/relatorio_de_controle.html',
            context=context,
            )

@admin.action(description="Relatório (Tabela) dos selecionados")
def export_excel(self, request, queryset):
    animals = []
    for animal in queryset:
        animal_data = animal.__dict__

        animal_data['especie'] = animal.especie.__dict__

        # Relatorio
        relatorio = animal.relatorio
        animal_data['relatorio'] = relatorio.__dict__
        animal_data['relatorio']['local_resgate'] = relatorio.local_resgate.__dict__
        relatorio_fks = ['origem', 'motivo']
        for relatorio_fk in relatorio_fks:
            obj = getattr(relatorio, relatorio_fk, None)
            if obj is not None:
                animal_data['relatorio'][relatorio_fk] = obj.__dict__
        animal_data['relatorio']['local_resgate']['endereco'] = relatorio.local_resgate.endereco.__dict__

        # Status
        if animal.status is not None:
            animal_data['status'] = animal.status.__dict__

        animals.append(animal_data)

    animals_excel = {
            'Data': [],
            'Código do animal': [],
            'Grupo': [],
            'Espécie': [],
            'Nome Popular': [],
            'Sexo': [],
            'Faixa etária': [],
            'Estado geral': [],
            'B.O.': [],
            'Controle recebimento IPEVS': [],
            'Origem': [],
            'Motivo': [],
            'Termo de Destinação': [],
            'Área resgate': [],
            'Munícipio de Origem': [],
            'Endereço': [],
            'Longitude': [],
            'Latitude': [],
            'Chip': [],
            'Anilha': [],
            'Recomendação': [],
            'Observações': [],
            'Data da Saída': [],
            'Imagem': [],
            }

    for animal_data in animals:
        animals_excel['Data'].append(f"{animal_data['data_entrada']}")
        animals_excel['Código do animal'].append(f"{animal_data['codigo_interno']}")
        animals_excel['Grupo'].append(f"{animal_data['especie']['classe']}")
        animals_excel['Espécie'].append(f"{animal_data['especie']['nome_cientifico']}")
        animals_excel['Nome Popular'].append(f"{animal_data['especie']['nome_popular']}")
        animals_excel['Sexo'].append(f"{animal_data['sexo']}")
        animals_excel['Faixa etária'].append(f"{animal_data['faixa_etaria']}")
        animals_excel['Estado geral'].append(f"{animal_data['condicao_fisica']}")
        animals_excel['B.O.'].append(f"{animal_data['relatorio']['bo']}")
        animals_excel['Controle recebimento IPEVS'].append(f"")
        animals_excel['Origem'].append(f"{animal_data['relatorio']['origem']['descricao']}")
        animals_excel['Motivo'].append(f"{animal_data['relatorio']['motivo']['descricao']}")
        animals_excel['Termo de Destinação'].append(f"{animal_data['relatorio']['termo_destinacao']}")
        animals_excel['Área resgate'].append(f"{animal_data['relatorio']['local_resgate']['area_resgate']}")
        animals_excel['Munícipio de Origem'].append(f"{animal_data['relatorio']['local_resgate']['municipio']}")
        animals_excel['Endereço'].append(f"{animal_data['relatorio']['local_resgate']['endereco']['rua']}, {animal_data['relatorio']['local_resgate']['endereco']['numero']} - {animal_data['relatorio']['local_resgate']['endereco']['bairro']},  {animal_data['relatorio']['local_resgate']['endereco']['complemento']}")
        animals_excel['Longitude'].append(f"{animal_data['relatorio']['local_resgate']['longitude']}")
        animals_excel['Latitude'].append(f"{animal_data['relatorio']['local_resgate']['latitude']}")
        animals_excel['Chip'].append("")
        animals_excel['Anilha'].append("")
        animals_excel['Recomendação'].append(f"{animal_data['status']['status']}")
        animals_excel['Observações'].append(f"{animal_data['status']['observacao']}")
        animals_excel['Data da Saída'].append(f"{animal_data['status']['data_saida']}")
        animals_excel['Imagem'].append("")
    df = pd.DataFrame(data=animals_excel)

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        df.to_excel(writer,
                    index=False, 
                    encoding='utf8',
                    sheet_name="Animals",
                    )
    now = datetime.now(tz=timezone('America/Sao_Paulo'))
    response = http.HttpResponse(buffer.getvalue(),
                                 content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'inline; filename=animals_{now}.xlsx'
    return response