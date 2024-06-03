from django.db import models

class Company(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    last_fetch = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
