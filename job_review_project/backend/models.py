from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=NULL)

    def __str__(self):
        return self.name