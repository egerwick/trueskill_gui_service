# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-30 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.CharField(blank=True, default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GamePerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField(default=0)),
                ('owngoals', models.IntegerField(blank=True, default=0, null=True)),
                ('playerposition', models.CharField(blank=True, default=b'', max_length=100)),
                ('winner', models.BooleanField(default=False)),
                ('crawling', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, default=b'', max_length=100)),
                ('mu', models.FloatField(default=25.0)),
                ('sigma', models.FloatField(default=8.33333)),
            ],
        ),
        migrations.AddField(
            model_name='gameperformance',
            name='player',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1def',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1def_per', to='hello.GamePerformance'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1of',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1of_per', to='hello.GamePerformance'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2def',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2def_per', to='hello.GamePerformance'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2of',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2of_per', to='hello.GamePerformance'),
        ),
    ]
