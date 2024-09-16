# Generated by Django 5.0.6 on 2024-09-16 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_rename_model_legkovoe_avto_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Legkovoe_Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('avto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.legkovoe_avto')),
            ],
        ),
    ]
