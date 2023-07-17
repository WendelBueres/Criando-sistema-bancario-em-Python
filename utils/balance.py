import data
import locale

def balance():
    print(
        f'Saldo atual: {format(locale.currency(data.balance))}'
    )