# Generated by Django 5.2.1 on 2025-06-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_literarium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
