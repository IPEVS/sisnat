from django import forms

from . import models


class EcdiseForm(forms.ModelForm):
    class Meta:
        model = models.Ecdise
        fields = '__all__'

    def clean_classe(self):
        animal = self.cleaned_data.get('animal')
        if animal is None:
            raise forms.ValidationError('Animal não informado')
        classe = self.cleaned_data.get('classe')
        if classe is None:
            raise forms.ValidationError('Classe não informada')
        if animal.especie.classe != classe:
            raise forms.ValidationError(
                    'A classe informada é diferente da classe do animal')
        return classe


class MorfometriaForm(forms.ModelForm):
    class Meta:
        model = models.Morfometria
        fields = '__all__'

    def clean_classe(self):
        animal = self.cleaned_data.get('animal')
        if animal is None:
            raise forms.ValidationError('Animal não informado')
        classe = self.cleaned_data.get('classe')
        if classe is None:
            raise forms.ValidationError('Classe não informada')
        if animal.especie.classe != classe:
            raise forms.ValidationError(
                    'A classe informada é diferente da classe do animal')
        return classe
