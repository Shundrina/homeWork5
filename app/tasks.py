from datetime import datetime

import requests
from celery import shared_task, chain

from app.models import Currency


@shared_task
def parse_privat():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')

    return response.json()


@shared_task
def save_course(result):

    for el in result:
        currency = Currency()
        currency.time = datetime.now()
        currency.ccy = el['ccy']
        currency.base_ccy = el['base_ccy']
        currency.buy = el['buy']
        currency.sale = el['sale']
        currency.save()

    return result


@shared_task
def chain_task():
    chain(
        parse_privat.s()
        |
        save_course.s()
    )()
