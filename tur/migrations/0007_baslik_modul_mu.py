# Generated by Django 2.0 on 2019-08-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tur', '0006_dersler_baslık'),
    ]

    operations = [
        migrations.AddField(
            model_name='baslik',
            name='modul_mu',
            field=models.BooleanField(default=False, verbose_name='Modül mü'),
        ),
    ]
