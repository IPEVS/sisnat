# Generated by Django 4.0.3 on 2022-04-14 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('codigo_interno', models.CharField(max_length=30, unique=True, verbose_name='Código Interno')),
                ('data_entrada', models.DateField(verbose_name='Data de entrada')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('sexo', models.CharField(choices=[('FÊMEA', 'Fêmea'), ('MACHO', 'Macho'), ('INDEFINIDO', 'Indefinido')], default='INDEFINIDO', max_length=10, verbose_name='Sexo')),
                ('faixa_etaria', models.CharField(choices=[('FILHOTE', 'Filhote'), ('JOVEM', 'Jovem'), ('ADULTO', 'Adulto')], max_length=7, verbose_name='Faixa etária')),
                ('condicao_fisica', models.CharField(choices=[('BOA', 'Boa'), ('ÓTIMA', 'Ótima'), ('REGULAR', 'Regular'), ('RUIM', 'Ruim'), ('PÉSSIMA', 'Péssima')], default='BOA', max_length=7, verbose_name='Condição Física')),
                ('esta_vivo', models.BooleanField(default=True, verbose_name='O animal está vivo?')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animais',
            },
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do doador')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Doador',
                'verbose_name_plural': 'Doadores',
            },
        ),
        migrations.CreateModel(
            name='EspecieAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('classe', models.CharField(choices=[('AMPHIBIA', 'Amphibia'), ('ARACHNIDA', 'Arachnida'), ('AVES', 'Aves'), ('MAMMALIA', 'Mammalia'), ('REPTILIA', 'Reptilia')], max_length=9, verbose_name='Classe do animal')),
                ('nome_cientifico', models.CharField(max_length=100, verbose_name='Nome Científico')),
                ('nome_popular', models.CharField(max_length=100, verbose_name='Nome Popular')),
            ],
            options={
                'verbose_name': 'Especie do Animal',
                'verbose_name_plural': 'Especie dos Animais',
            },
        ),
        migrations.CreateModel(
            name='LocalResgate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('longitude', models.FloatField(blank=True, max_length=12, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, max_length=12, null=True, verbose_name='Latitude')),
                ('municipio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Município de origem')),
                ('endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço')),
                ('area_resgate', models.CharField(blank=True, max_length=50, null=True, verbose_name='Área do resgate')),
            ],
            options={
                'verbose_name': 'Local do Resgate',
                'verbose_name_plural': 'Locais do Resgate',
            },
        ),
        migrations.CreateModel(
            name='MotivoResgate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('descricao', models.CharField(max_length=80, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Motivo',
                'verbose_name_plural': 'Motivos',
            },
        ),
        migrations.CreateModel(
            name='OrigemAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Origem do Animal',
                'verbose_name_plural': 'Origem do Animais',
            },
        ),
        migrations.CreateModel(
            name='RelatorioAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('bo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Boletim de ocorrência')),
                ('termo_destinacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Termo de destinação')),
                ('soltura', models.TextField(blank=True, null=True, verbose_name='Soltura')),
                ('local_resgate', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='animal.localresgate', verbose_name='Local de Resgate do Animal')),
                ('motivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animal.motivoresgate', verbose_name='Motivo do resgate do Animal')),
                ('origem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animal.origemanimal', verbose_name='Origem do Animal')),
            ],
            options={
                'verbose_name': 'Relatório do Animal',
                'verbose_name_plural': 'Relatórios dos Animais',
            },
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('data_observacao', models.DateField(verbose_name='Data da observação')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal', verbose_name='Codigo Interno')),
            ],
            options={
                'verbose_name': 'Observação',
                'verbose_name_plural': 'Observações',
            },
        ),
        migrations.CreateModel(
            name='Morfometria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('classe', models.CharField(choices=[('AMPHIBIA', 'Amphibia'), ('ARACHNIDA', 'Arachnida'), ('AVES', 'Aves'), ('MAMMALIA', 'Mammalia'), ('REPTILIA', 'Reptilia')], max_length=9, verbose_name='Classe do animal')),
                ('data_medicao', models.DateField(verbose_name='Data da medição')),
                ('cc', models.CharField(blank=True, max_length=30, null=True, verbose_name='Comprimento da Calda')),
                ('cf', models.CharField(blank=True, max_length=30, null=True)),
                ('cp', models.CharField(blank=True, max_length=30, null=True)),
                ('cpp', models.CharField(blank=True, max_length=30, null=True)),
                ('crc', models.CharField(blank=True, max_length=30, null=True)),
                ('ct', models.CharField(blank=True, max_length=30, null=True)),
                ('cta', models.CharField(blank=True, max_length=30, null=True)),
                ('don', models.CharField(blank=True, max_length=30, null=True)),
                ('peso', models.CharField(blank=True, max_length=30, null=True)),
                ('ca', models.CharField(blank=True, max_length=30, null=True)),
                ('cb', models.CharField(blank=True, max_length=30, null=True)),
                ('h', models.CharField(blank=True, max_length=30, null=True)),
                ('cm', models.CharField(blank=True, max_length=30, null=True)),
                ('cra', models.CharField(blank=True, max_length=30, null=True)),
                ('ho', models.CharField(blank=True, max_length=30, null=True)),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
            options={
                'verbose_name': 'Morfometria',
                'verbose_name_plural': 'Morfometria',
            },
        ),
        migrations.CreateModel(
            name='FichaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('data_procedimento', models.DateField(verbose_name='Data da observação')),
                ('procedimento', models.TextField(blank=True, null=True, verbose_name='Procedimento')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal', verbose_name='Codigo Interno')),
            ],
            options={
                'verbose_name': 'Ficha Clínica',
                'verbose_name_plural': 'Fichas Clínicas',
            },
        ),
        migrations.CreateModel(
            name='Ecdise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('classe', models.CharField(choices=[('AMPHIBIA', 'Amphibia'), ('ARACHNIDA', 'Arachnida'), ('AVES', 'Aves'), ('MAMMALIA', 'Mammalia'), ('REPTILIA', 'Reptilia')], max_length=9, verbose_name='Classe do animal')),
                ('data_ecdise', models.DateField(verbose_name='Data da ecdise')),
                ('ecdise', models.CharField(choices=[('COMPLETA', 'Completa'), ('INCOMPLETA', 'Incompleta')], default='INCOMPLETA', max_length=10)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
            options={
                'verbose_name': 'Ecdise',
                'verbose_name_plural': 'Ecdise',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='doador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animal.doador', verbose_name='Doador'),
        ),
        migrations.AddField(
            model_name='animal',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='animal.especieanimal', verbose_name='Tipo do animal'),
        ),
        migrations.AddField(
            model_name='animal',
            name='relatorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='animal.relatorioanimal', verbose_name='Relatorio'),
        ),
        migrations.CreateModel(
            name='Alimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('data_alimentacao', models.DateField(verbose_name='Data da alimentação')),
                ('alimento', models.CharField(max_length=200, verbose_name='Alimento')),
                ('unidade_de_medida', models.CharField(blank=True, max_length=20, null=True, verbose_name='Unidade de medida')),
                ('quantidade', models.FloatField(blank=True, null=True)),
                ('sobra', models.CharField(blank=True, max_length=200, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal', verbose_name='Código Interno')),
            ],
            options={
                'verbose_name': 'Alimentação',
                'verbose_name_plural': 'Alimentações',
            },
        ),
    ]
