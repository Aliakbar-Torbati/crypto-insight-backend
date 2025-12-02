from django.db import models

# Create your models here.

class Coin(models.Model):

    symbol = models.CharField(
        max_length=10,
        unique=True,
        help_text="Short symbol of the coin, e.g. BTC, ETH."
    )
    name = models.CharField(
        max_length=50,
        help_text="Full name of the coin, e.g. Bitcoin."
    )

    def __str__(self):
        """
        This is how the object will be shown in admin and shell.
        """
        return f"{self.name} ({self.symbol})"

