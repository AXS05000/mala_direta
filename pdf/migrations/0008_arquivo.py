# Generated by Django 4.1.9 on 2023-07-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0007_funcionario_dsr_feriado_funcionario_qtde_dsr_feriado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('competencia', models.CharField(max_length=200)),
            ],
        ),
    ]