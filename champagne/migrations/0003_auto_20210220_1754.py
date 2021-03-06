# Generated by Django 2.2.14 on 2021-02-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champagne', '0002_auto_20210220_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champagne',
            name='brand',
            field=models.CharField(db_index=True, max_length=25, unique=True, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='champagne',
            name='champ_type',
            field=models.IntegerField(choices=[(2, 'Extra Dry'), (1, 'Brut'), (5, 'Doux'), (4, 'Demi-Sec'), (3, 'Dry')], verbose_name='Champagne Type'),
        ),
    ]
