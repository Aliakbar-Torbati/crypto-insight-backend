
from django.contrib import admin
from django.urls import path
from market.views import CoinListView   # import our API view


urlpatterns = [
    path('admin/', admin.site.urls),

        # REST API endpoint for listing coins
    path("api/v1/coins/", CoinListView.as_view(), name="coins-list"),
]
