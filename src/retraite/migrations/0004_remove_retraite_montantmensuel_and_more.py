# Generated by Django 5.1.4 on 2025-01-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retraite', '0003_banque_alter_retraitedeces_assignationdefunt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retraite',
            name='montantMensuel',
        ),
        migrations.AlterField(
            model_name='retraite',
            name='nPension',
            field=models.IntegerField(unique=True),
        ),
    ]
