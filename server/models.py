from django.db import models


# DB model for stocks. Will contain all the details about the stock
class Stock(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    adj_close = models.FloatField()
    stock = models.CharField(max_length=10)

    def __str__(self):
        return self.stock
