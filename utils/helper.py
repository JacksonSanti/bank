from datetime import date
from datetime import datetime


def date_to_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_to_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_coin(valor: float) -> str:
    return f'R$ {valor:,.2f}'

