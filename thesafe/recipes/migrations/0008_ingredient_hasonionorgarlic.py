# Generated by Django 4.1.7 on 2023-02-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='hasOnionOrGarlic',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
