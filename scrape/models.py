from django.db import models

# Create your models here.
class InstaData(models.Model):

    username = models.CharField(max_length=50)
    data = models.JSONField()

    def __str__(self):
        return self.username