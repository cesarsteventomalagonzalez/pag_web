# Generated by Django 5.0.6 on 2024-06-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True, verbose_name='Empresa')),
                ('contacto', models.CharField(max_length=10)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/empresa')),
                ('promo', models.FileField(blank=True, null=True, upload_to='logo/empresa')),
                ('promo1', models.FileField(blank=True, null=True, upload_to='logo/empresa')),
                ('promo2', models.FileField(blank=True, null=True, upload_to='logo/empresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'ordering': ('nombre',),
            },
        ),
    ]
