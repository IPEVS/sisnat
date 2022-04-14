from animal.models import Animal

from django.shortcuts import render
from django.contrib import admin

@admin.action(description="Trocar animal selecionado como MORTO")
def animal_morto(modeladmin, request, queryset):
    queryset.update(esta_vivo=False)

@admin.action(description="Imprimir relatório dos selecionados")
def imprimir_relatorio(self, request, queryset):
    animal = Animal.objects.all()
    dados = {'animals': animal}
    return render(request, 'sisnat/pdf_page.html/', dados)