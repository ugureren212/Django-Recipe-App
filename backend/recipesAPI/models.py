from django.db import models

class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    cooking_time = models.DurationField()
    total_time = models.DurationField()
    difficulty_level = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Model to represent the relationship between Recipe and Ingredient
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    measurement_unit = models.CharField(max_length=20)