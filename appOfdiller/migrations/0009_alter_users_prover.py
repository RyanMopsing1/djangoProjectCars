# Generated by Django 5.1.5 on 2025-03-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOfdiller', '0008_users_prover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='prover',
            field=models.BooleanField(verbose_name='Обработка данных'),
        ),
    ]
