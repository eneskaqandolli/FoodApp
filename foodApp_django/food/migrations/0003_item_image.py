# Generated by Django 5.0.3 on 2024-07-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
