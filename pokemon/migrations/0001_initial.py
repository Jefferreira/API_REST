# Generated by Django 3.2.5 on 2021-07-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=127)),
                ('tipos', models.CharField(max_length=127)),
                ('imagem_origem', models.URLField(max_length=127)),
            ],
        ),
    ]
