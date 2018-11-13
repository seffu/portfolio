from django.db import models

# Create your models here.
class Job(models.Model):
    summary = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.summary
