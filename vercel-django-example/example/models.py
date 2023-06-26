from django.db import models

class Document(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.TextField(blank=True)
    content = models.TextField()

class Image(models.Model):
    parent = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='children')
    image = models.ImageField(upload_to='child_images/')
    created_at = models.DateTimeField(auto_now_add=True)

