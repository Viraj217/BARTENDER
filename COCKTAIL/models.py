from django.db import models

# Create your models here.
class drink_model(models.Model):
    drink_name = models.CharField(unique=True)
    drink_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.drink_name} ({self.drink_count})"
