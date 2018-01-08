# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=35, default='')),
                ('District', models.CharField(max_length=20, default='')),
                ('Population', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('Code', models.CharField(primary_key=True, max_length=3, blank=None, default='', serialize=False)),
                ('Name', models.CharField(max_length=52, default='')),
                ('Continent', models.CharField(max_length=30, default='Asia', choices=[('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('Africa', 'Africa'), ('Oceania', 'Oceania'), ('Antartica', 'Antartica'), ('South America', 'South America')])),
                ('Region', models.CharField(max_length=26, default='')),
                ('SurfaceArea', models.FloatField(default=0.0)),
                ('IndepYear', models.SmallIntegerField(blank=True, null=True, default=None)),
                ('Population', models.IntegerField(default=0)),
                ('LifeExpectancy', models.FloatField(blank=True, null=True, default=None)),
                ('GNP', models.FloatField(blank=True, null=True, default=None)),
                ('GNPOld', models.FloatField(blank=True, null=True, default=None)),
                ('LocalName', models.CharField(max_length=45, default='')),
                ('GovernmentForm', models.CharField(max_length=45, default='')),
                ('HeadOfState', models.CharField(max_length=60, blank=True, null=True, default=None)),
                ('Capital', models.IntegerField(null=True, default=None)),
                ('Code2', models.CharField(max_length=2, default='')),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='countrylanguage',
            fields=[
                ('countrylanguage_id', models.AutoField(primary_key=True, serialize=False)),
                ('Language', models.CharField(max_length=30, default='')),
                ('IsOfficial', models.CharField(max_length=1, default='F', choices=[('T', 'true'), ('F', 'false')])),
                ('Percentage', models.FloatField(default=0.0)),
                ('CountryCode', models.ForeignKey(db_column='CountryCode', to='customization.country')),
            ],
            options={
                'db_table': 'countrylanguage',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='CountryCode',
            field=models.ForeignKey(default='', db_column='CountryCode', to='customization.country'),
        ),
        migrations.AlterUniqueTogether(
            name='countrylanguage',
            unique_together=set([('CountryCode', 'Language')]),
        ),
    ]
