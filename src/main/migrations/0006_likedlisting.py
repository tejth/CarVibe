# Generated by Django 5.1.6 on 2025-02-14 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_listing_brand'),
        ('users', '0006_alter_profile_location_alter_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listing')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
