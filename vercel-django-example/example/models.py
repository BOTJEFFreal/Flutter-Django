from django.db import models

class Image(models.Model):
    def nameFile(instance, filename):
     return '/'.join(['images', str(instance.name), filename])
    # folder_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to=nameFile)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
