# Generated by Django 4.0.3 on 2022-04-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_realtor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_approved',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100),
        ),
    ]
