# Generated by Django 4.1.7 on 2023-02-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(null=True, upload_to='recipe_images'),
        ),
    ]
