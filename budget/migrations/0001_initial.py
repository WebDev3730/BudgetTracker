# Generated by Django 5.1.4 on 2024-12-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('food', 'Food'), ('Enterntainment', 'Entertainment'), ('Utility', 'Utility'), ('other', 'Other')], max_length=50)),
                ('transaction_type', models.CharField(choices=[('income', 'income'), ('expense', 'Expense')], max_length=7)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
