# Generated by Django 5.0.6 on 2024-05-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
