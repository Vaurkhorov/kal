# Generated by Django 4.1.7 on 2023-02-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_ingredient_hasonionorgarlic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(null=True, upload_to='assets/recipe_images/'),
        ),
    ]
