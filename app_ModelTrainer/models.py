from django.db import models


class ConfidentImage(models.Model):
    image_name = models.CharField(max_length=255)
    image_path = models.TextField()
    classified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    

class NonConfidentImage(models.Model):
    image_name = models.CharField(max_length=255)
    image_path = models.TextField()
    classified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name