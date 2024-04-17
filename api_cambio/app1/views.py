# -*- coding: utf-8 -*-
# coding: utf-8

from django.http import JsonResponse
from forex_python.converter import CurrencyRates


def convert_currency(request):
    currency_rate = CurrencyRates()

    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = request.GET.get('amount')

    # Fazer teste se os codigos estão corretos
    # Fazer teste se o valor é um número real inteiro ou float

    if not from_currency or not to_currency or not amount:
        return JsonResponse({'error': 'Parâmetros inválidos'}, status=400)

    try:
        # Fazer arrendondamento dos centavos?
        converted_amount = currency_rate.convert(from_currency, to_currency, float(amount))
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'from': from_currency, 'to': to_currency, 'amount': amount, 'converted_amount': converted_amount})
