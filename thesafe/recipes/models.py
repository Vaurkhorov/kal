from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         ordering = ('name', )
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name

    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    isVegan = models.BooleanField()
    hasDairy = models.BooleanField()
    hasNuts = models.BooleanField()
    hasGluten = models.BooleanField()

    class Meta:
        ordering = ("name", )
        verbose_name_plural = "Ingredients"
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient)

    class Meta:
        ordering = ("name", )
        verbose_name_plural = "Recipes"
    
    def __str__(self):
        return self.name