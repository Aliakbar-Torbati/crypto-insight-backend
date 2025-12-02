from django.contrib import admin
from .models import Coin

# This makes the Coin model appear in the Django admin interface
@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    """
    Configuration for how Coin is displayed in the admin panel.
    """
    list_display = ("id", "symbol", "name")   # columns in the list view
    search_fields = ("symbol", "name")        # search box on top