from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone = models.PositiveIntegerField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
