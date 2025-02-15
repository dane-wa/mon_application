# Generated by Django 5.1.4 on 2025-01-08 13:45

import django.db.models.deletion
import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeEmployeur', models.CharField(max_length=10)),
                ('nomEmployeur', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codePrefecture', models.CharField(max_length=10)),
                ('nomPrefecture', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Retraite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nPension', models.IntegerField(max_length=10, unique=True)),
                ('titre', models.CharField(choices=[('Mr', 'Monsieur'), ('Mme', 'Madame')], max_length=3)),
                ('prenom', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('01-', 'Retraite')], max_length=10)),
                ('dateNais', models.DateField()),
                ('dateJouis', models.DateField()),
                ('montantTrim', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allocation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MensuelDu', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('montantTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montantTrim_40', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montantComp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Observation', models.TextField(blank=True, max_length=200)),
                ('montantMensuel', models.GeneratedField(db_persist=True, expression=models.Case(models.When(models.Q(('montantTrim_40__gte', 264000.0), ('montantTrim_40__lte', 616000.0)), then=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('montantTrim_40'), '*', models.Value(2.2)), '/', models.Value(3))), models.When(models.Q(('montantTrim_40__gt', 616000.0), ('montantTrim_40__lte', 1537099.0)), then=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('montantTrim_40'), '*', models.Value(1.85)), '/', models.Value(3))), models.When(montantTrim_40__gt=1537099.0, then=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('montantTrim_40'), '*', models.Value(1.5)), '/', models.Value(3))), output_field=models.DecimalField(decimal_places=2, max_digits=10)), output_field=models.DecimalField(decimal_places=2, max_digits=10))),
                ('image', models.ImageField(blank=True, null=True, upload_to='retraites_images/%Y/%m/%d/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retraite.employeur')),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retraite.prefecture')),
            ],
        ),
    ]
