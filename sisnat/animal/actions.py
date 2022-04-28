from datetime import datetime

from django.shortcuts import render
from django.contrib import admin
from pytz import timezone

from core import utils
from animal import models


@admin.action(description="Trocar animais selecionados para morto")
def animal_morto(modeladmin, request, queryset):
    queryset.update(esta_vivo=False)


@admin.action(description="Imprimir relatório dos selecionados")
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
