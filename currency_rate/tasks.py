import aiohttp
import asyncio
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_project.settings")
django.setup()
from celery import shared_task
import asyncio
import aiohttp
from asgiref.sync import sync_to_async
from currency_rate.models import Currency


@sync_to_async
def create_currency(currency_name, usd_to_rub_rate):
    conversion = Currency.objects.create(
        currency_name=currency_name,
        usd_to_rub_rate=usd_to_rub_rate
    )
    return conversion


@shared_task
def update_currency():
    api_key = '58cf8eefee2419244c06c43213de050118518ce1'
    from_currency = 'USD'
    to_currency = 'RUB'
    amount = 1

    async def fetch_data():
        base_url = 'https://api.getgeoapi.com/v2/currency/convert'

        url = f'{base_url}?api_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}&format=json'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                currency_name = data['rates']['RUB']['currency_name']
                usd_to_rub_rate = data['rates']['RUB']['rate']
                await create_currency(currency_name=currency_name, usd_to_rub_rate=usd_to_rub_rate)

    asyncio.run(fetch_data())
