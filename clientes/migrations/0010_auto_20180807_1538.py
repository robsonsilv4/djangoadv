# Generated by Django 2.0.7 on 2018-08-07 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20180803_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'permissions': (('deletar_clientes', 'Permissão para deletar clientes'),)},
        ),
    ]
