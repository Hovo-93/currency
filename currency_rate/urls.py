from django.urls import path
from currency_rate.views import CurrencyList


urlpatterns = [
    path('get-current-usd/', CurrencyList.as_view(), name='currency_list'),

]