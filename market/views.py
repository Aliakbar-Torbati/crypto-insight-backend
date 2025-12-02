from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coin
from .serializers import CoinSerializer

class CoinListView(APIView):
    """
    GET /api/v1/coins/

    Returns a list of all available coins in JSON format.
    Example response:
    [
        {"id": 1, "symbol": "BTC", "name": "Bitcoin"},
        {"id": 2, "symbol": "ETH", "name": "Ethereum"}
    ]
    """

    def get(self, request):
        # 1. Query all Coin objects from the database
        coins = Coin.objects.all()

        # 2. Serialize them into Python dicts/lists
        serializer = CoinSerializer(coins, many=True)

        # 3. Return them as a JSON HTTP response
        return Response(serializer.data)

