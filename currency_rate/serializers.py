from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from currency_rate.models import Currency


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            'currency_name',
            'usd_to_rub_rate',
            'created_at',
        )
