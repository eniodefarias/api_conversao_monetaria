# -*- coding: utf-8 -*-
# coding: utf-8

from django.http import JsonResponse
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
# from forex_python.bitcoin import CryptoCurrencies

#https://docs.awesomeapi.com.br/api-de-moedas
#https://theforexapi.com/documentation/
#http://127.0.0.1:8000/cambio_forex/?from=ETH&to=BRL&amount=1

def convert_currency(request):
    currency_rate = CurrencyRates()
    btc_converter = BtcConverter()

    # USD
    # BRL
    # EUR
    # BTC
    # ETH

    from_currency = str(request.GET.get('from')).upper()
    to_currency = str(request.GET.get('to')).upper()
    amount = float(str(request.GET.get('amount')).replace(',','.'))

    if not from_currency or not to_currency or not amount:
        return JsonResponse({'error': 'Parâmetros inválidos'}, status=400)

    try:
        lastro = 'USD'
        print(f'001  -  ')
        if from_currency == 'ETH' or to_currency == 'ETH':
            print(f'002  -  ')
            raise Exception(' Forex não tem acesso ao ETH :( ')
        elif from_currency == 'BTC' or to_currency == 'BTC':
            print(f'003  -  ')
            value_BTC_to_USD = btc_converter.get_latest_price(lastro)
            print(f'004  -  value_BTC_to_USD={value_BTC_to_USD}')

        print(f'005  -  ')
        if from_currency != 'BTC':
            print(f'006  -  ')
            value_USD_from = currency_rate.convert(lastro, from_currency, float(1))
            print(f'007  -  ')
        else:
            print(f'008  -  ')
            value_USD_from = value_BTC_to_USD
            print(f'009  -  ')

        print(f'010  -  ')
        if to_currency != 'BTC':
            print(f'011  -  ')
            value_USD_to = currency_rate.convert(lastro, to_currency, float(1))
            print(f'012  -  ')
        else:
            print(f'013  -  ')
            value_USD_to = value_BTC_to_USD
            print(f'014  -  ')

        print(f'015  -  ')

        cotacao = round(value_USD_to / value_USD_from * amount, 4)
        print(f'016  -  cotacao={cotacao}')

        converted_amount = cotacao

    except Exception as e:
        # if from_currency == 'ETH' or to_currency == 'ETH':
        #     return JsonResponse({'error': str(e + ' Forex não tem acesso ao ETH :( ')}, status=400)
        # else:

        return JsonResponse({'error': str(e)}, status=400)

    # return JsonResponse({})
    return JsonResponse({'from': from_currency, 'to': to_currency, 'amount': amount, 'converted_amount': converted_amount
                         # f'cotacao_{from_currency}_to_{to_currency}': cotacao,
                         # f'from_USD_to_{from_currency}': value_USD_from,
                         # f'to_USD_to_{to_currency}': value_USD_to
                         })
