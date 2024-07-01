# Generated by Django 5.0.6 on 2024-06-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_producto_delete_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('foto', models.FileField(blank=True, null=True, upload_to='logo/empresa')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('numero_whatsapp', models.CharField(default='+593959682902', max_length=15)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]