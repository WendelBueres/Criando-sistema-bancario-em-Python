import locale
import datetime
from data import accounts

def withdraw(account_id, value):
    try:    
        account = None

        if not account_id:
            print('Você precisa informar o número da conta para realizar um saque.')
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

        done = False

        if value == 'C' or value == 'c':
            print('Operação cancelada.')

            done = True

        if (account['last_withdraw'] != datetime.date.today()):
            account['last_withdraw'] = datetime.date.today()
            account['count_withdraw'] = 0

        if (account['last_withdraw'] == datetime.date.today() and account['count_withdraw'] == 3):
            print('''
Você atingiu o limite de saques de hoje.
            ''')
            raise ValueError()

        while not done:
            try:
                value = float(value)

                if (value < 0):
                    print('''
O valor do saque não pode ser negativo.
                    ''')
                    raise ValueError()

                if (value > account['balance']):
                    print('''
O valor do saque é maior que o saldo disponível.
Verifique o saldo e tente novamente.
                    ''')
                    raise ValueError()
                
                account['balance'] = (account['balance'] - value)

                account['extract'].append({
                    'operation': 'Saque',
                    'value': locale.currency(value),
                })

                done = True

                account['count_withdraw'] = account['count_withdraw'] + 1

            except:
                print('''
Ocorreu um erro ao efetuar o saque.
                    
Para cancelar o depósito, pressione [C].
                ''')
    
    except:
        print('''
Ocorreu um erro ao efetuar o saque.
        ''')