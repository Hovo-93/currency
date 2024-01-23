# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import CurrencySerializer
# api_key ='58cf8eefee2419244c06c43213de050118518ce1'
#
# req = 'https://api.getgeoapi.com/v2/ip/check?api_key={58cf8eefee2419244c06c43213de050118518ce1}&format={json}'
#
# # class GetCurrentUSDView(APIView):
# #     pass
import datetime

from rest_framework import generics, status

from currency_rate.models import Currency
from currency_rate.serializers import CurrencySerializer





class CurrencyList(generics.ListAPIView):
    """
        Список всех Currency
    """
    queryset = Currency.objects.order_by('created_at')[:10]
    serializer_class = CurrencySerializer