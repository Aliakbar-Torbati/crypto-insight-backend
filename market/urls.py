from django.contrib import admin
from django.urls import path
from market.views import CoinListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoint for coins
    path('api/v1/coinss/', CoinListView.as_view(), name='coins-list'),
]
