# Generated by Django 5.1.2 on 2024-10-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
                ('total_donations', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('last_donation_date', models.DateTimeField(blank=True, null=True)),
                ('preferred_donation_method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Bank Transfer', 'Bank Transfer')], default='Credit Card', max_length=50)),
                ('role', models.CharField(choices=[('individual', 'Individual'), ('corporate', 'Corporate'), ('organisation', 'Organisation')], max_length=15)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
