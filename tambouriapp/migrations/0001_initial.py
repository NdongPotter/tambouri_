# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peintre',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('surnom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tableau',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('prix_vente', models.IntegerField()),
                ('vendu', models.BooleanField(default='False')),
                ('quantite', models.IntegerField()),
                ('peintre', models.ForeignKey(to='tambouriapp.Peintre')),
            ],
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('numero', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('prix_vente', models.IntegerField()),
                ('vendu', models.BooleanField(default='False')),
                ('quantite', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('modele', models.CharField(max_length=100)),
                ('marque', models.CharField(max_length=100)),
                ('annee', models.DateTimeField()),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('prix_vente', models.IntegerField()),
                ('vendu', models.BooleanField(default='False')),
                ('quantite', models.IntegerField()),
            ],
        ),
    ]
