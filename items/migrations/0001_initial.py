# Generated by Django 5.0.6 on 2024-09-16 19:43

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marka_Legkovoe_Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Model_Legkovoe_Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.marka_legkovoe_avto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='items.transport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='marka_legkovoe_avto',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.transport'),
        ),
        migrations.CreateModel(
            name='Legkovoe_Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('deskription', models.TextField()),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('marka', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.marka_legkovoe_avto')),
                ('model', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.model_legkovoe_avto')),
                ('type', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.transport')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
