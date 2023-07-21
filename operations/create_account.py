from data import users, accounts
import time
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def create_account(user_id):
    try:
        user = None

        if not user_id:
            print('Você precisa informar o ID do usuário para criar uma conta.')
            raise ValueError()
        
        user_id = int(user_id)

        for user in users:
            if user['id'] == user_id:
                user = user
                break

            else:
                user = None

        if not user:
            print('\nUsuário não encontrado.')

            raise ValueError()            

        account = {
            'id': int(len(accounts) + 1),
            'agency': '0001',
            'balance': 0,
            'extract': [],
            'last_withdraw': None,
            'count_withdraw': 0,
            'user': user
        }


        accounts.append(account)

        print('\nConta criada com sucesso.')
        print(f'''
Dados da conta
    Agência: {account['agency']}
    Número da conta: {account['id']}

Dados do Titular 
    Nome: {account['user']['name']}
    CPF: {account['user']['cpf']}
    Data de nascimento: {account['user']['date_born'].strftime('%d/%m/%Y')}

Endereço do Titular
    Logradouro: {account['user']['address']['logradouro']}
    Número: {account['user']['address']['numero']}
    Bairro: {account['user']['address']['bairro']}
    Cidade: {account['user']['address']['cidade']}
    Estado: {account['user']['address']['estado']}
        	''')
    
    except:
        print('\nOcorreu um erro ao criar a conta.')
        print('Verifique se você inseriu um ID de usuário válido e tente novamente.')