import locale
from data import accounts

def balance(account_id):
    try:
        account = None

        if not account_id:
            print('Você precisa informar o número da conta para verificar o saldo.')
            raise ValueError()
        
        account_id = int(account_id)

        for account in accounts:
            if account["id"] == account_id:
                account = account
                break

            else:
                account = None

        if account == None:
            print('Conta não encontrada.')

            raise ValueError()

        print(
            f'Saldo atual da conta nº {account["id"]}: {format(locale.currency(account["balance"]))}'
        )
    
    except:
        print('''
Ocorreu um erro ao verificar o saldo da conta.
        ''')