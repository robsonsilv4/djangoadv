# Generated by Django 2.0.7 on 2018-07-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clientes_photos'),
        ),
    ]
