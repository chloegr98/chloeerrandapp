from django.db import models

# Create your models here.

# Model for an Errand that includes the name of the errand and whether it has been finished
class Errand(models.Model):
    name = models.CharField(max_length=250)
    finished = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name