from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coffee/', blank=True, null=True)  # ← Critical fix