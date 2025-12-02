from rest_framework import serializers
from .models import Coin

class CoinSerializer(serializers.ModelSerializer):
    """
    Serializes Coin instances to JSON and
    validates JSON data for creating/updating Coin objects.
    """
    class Meta:
        model = Coin
        fields = ['id', 'symbol', 'name']
