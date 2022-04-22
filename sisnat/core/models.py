from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    criado_em = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
