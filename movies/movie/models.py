from django.db import models

class movie(models.Model):
    title = models.CharField(max_length=20 , null=False)
    release_date = models.IntegerField()
    description = models.TextField(null=True)
    active = models.BooleanField(null=False)

    def __str__(self):
        return self.title