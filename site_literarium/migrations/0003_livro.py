# Generated by Django 5.2 on 2025-06-15 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_literarium', '0002_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('quantidade', models.PositiveIntegerField()),
                ('sinopse', models.TextField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capas/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_literarium.autor')),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_literarium.genero')),
            ],
        ),
    ]
