# Generated by Django 2.2.5 on 2019-09-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amadon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
