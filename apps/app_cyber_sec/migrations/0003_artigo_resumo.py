# Generated by Django 4.0.2 on 2022-06-04 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cyber_sec', '0002_artigo_referencias'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='resumo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
