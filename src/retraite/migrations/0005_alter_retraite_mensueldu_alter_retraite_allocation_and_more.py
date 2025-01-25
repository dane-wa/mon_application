# Generated by Django 5.1.4 on 2025-01-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retraite', '0004_remove_retraite_montantmensuel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retraite',
            name='MensuelDu',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='retraite',
            name='allocation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retraite',
            name='montantComp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retraite',
            name='montantTotal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retraite',
            name='montantTrim',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retraite',
            name='montantTrim_40',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
