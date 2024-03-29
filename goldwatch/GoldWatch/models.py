from django.db import models

# Create your models here.

class GoldCard(models.Model):
    date = models.DateField()
    price = models.FloatField(max_length = 200)
    weight = models.FloatField(max_length = 200)
    total_price_spend = models.FloatField(max_length = 200)
    total_weight_spend = models.FloatField(max_length = 200)