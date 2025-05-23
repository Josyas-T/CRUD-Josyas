# Generated by Django 5.2 on 2025-04-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro_cliente',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=18)),
                ('nome', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=2)),
                ('pais', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
