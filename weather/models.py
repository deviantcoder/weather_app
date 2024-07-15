from django.db import models
from uuid import uuid4


class City(models.Model):
    name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'
        # ordering = ['created']
