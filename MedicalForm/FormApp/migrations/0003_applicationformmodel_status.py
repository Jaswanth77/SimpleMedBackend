# Generated by Django 4.2.2 on 2023-07-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0002_rename_aadhar_card_applicationformmodel_aadhaar_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformmodel',
            name='status',
            field=models.CharField(blank=True, choices=[('applied', 'applied'), ('discontinued', 'discontinued'), ('admitted', 'admitted')], max_length=100, null=True),
        ),
    ]
