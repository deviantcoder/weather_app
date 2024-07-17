from django.db import models
from uuid import uuid4
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField(default=0, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'
        # ordering = ['created']

    def time_delta(self): # returns True if 1h has passed, else: False
        now = timezone.now()
        last_updated = self.updated if self.updated else self.created

        time_dif = now - last_updated
        return 1 if time_dif >= timezone.timedelta(hours=1) else 0
