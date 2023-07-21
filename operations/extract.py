import locale
from data import accounts

def extract(account_id):
    try:
        account = None

        if not account_id:
            print('Você precisa informar o número da conta para verificar o extrato.')
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

        registro = 1

        print(f'''
    Dados da Conta:
        Agência: {account['agency']}
        Número da conta: {account['id']}
        Titular: {account['user']['name']}
        '''          
    )

        print('-------------- Extrato --------------')

        if extract == []:
            print('''
    Não foram realizadas operações.
            ''')
        
        for operation in account['extract']:
            print(f'''
    Registro: {registro}
    Operação: {operation['operation']}
    Valor: {operation['value']}
            ''')



            registro += 1

        if extract != []:
            print(f'''
    -------------------------------------
    Saldo da conta: {format(locale.currency(account['balance']))}

    *** Fim do Extrato ***
            ''')

    except:
        print('''
Ocorreu um erro ao verificar o extrato da conta.
        ''')    