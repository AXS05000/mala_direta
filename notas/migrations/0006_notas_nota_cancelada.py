# Generated by Django 4.1.9 on 2023-09-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0005_alter_basecnpj_iss_alter_notas_baseinfocontratos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='nota_cancelada',
            field=models.BooleanField(default=False, verbose_name='Nota Cancelada?'),
            preserve_default=False,
        ),
    ]
