# Generated by Django 2.0 on 2019-08-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tur', '0007_baslik_modul_mu'),
    ]

    operations = [
        migrations.AddField(
            model_name='baslik',
            name='icon_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Icon ismi'),
        ),
    ]
