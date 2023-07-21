import locale
from data import accounts

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def deposit(account_id):
    try:
        account = None

        if not account_id:
            print('Você precisa informar o número da conta para realizar um depósito.')
            raise ValueError()
        
        account_id = int(account_id)

        for account in accounts:
            if account["id"] == account_id:
                account = account

                print(account)
                break

            else:
                account = None

        if account == None:
            print('Conta não encontrada.')

            raise ValueError()
        
        print (f'''
Confirme os dados da conta para depósito:
    Agência: {account['agency']}
    Número da conta: {account['id']}
    Titular: {account['user']['name']}

    Caso os dados estejam incorretos, pressione [C] para cancelar o depósito.
                ''')

        done = False

        while not done:
            try:
                value = input('Valor do depósito: ')

                if value == 'C' or value == 'c':
                    done = True

                value = float(value)

                if (value < 0):
                    print('''
    O valor do depósito não pode ser negativo.
                    ''')
                    raise ValueError()
                
                account['balance'] = (account['balance'] + value)

                account['extract'].append({
                    'operation': 'Depósito',
                    'value': locale.currency(value),
                })

                done = True

            except:
                print('''
Ocorreu um erro ao depositar o valor.
Verifique se você inseriu um valor válido e tente novamente.
                    
Para cancelar o depósito, pressione [C].
                ''')

    except:
                print('''
Ocorreu um erro ao depositar o valor.
                ''')
