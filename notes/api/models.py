from django.db import models

# Create your models here.
#basically class with data structure

class Note(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
    class Meta:
        ordering =['-updated'] #lastest updated item will be at the top