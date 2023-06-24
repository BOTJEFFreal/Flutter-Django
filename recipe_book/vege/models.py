from django.db import models

# Create your models here.
class Recipes(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe_images")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.recipe_name[0:50]
    
    class Meta:
        ordering =['-updated'] #lastest updated item will be at the top

