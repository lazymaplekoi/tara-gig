# Generated by Django 4.2 on 2023-10-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0005_venue_display_name_alter_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
