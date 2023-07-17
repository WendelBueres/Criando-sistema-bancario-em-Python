import data
import locale

def withdraw():
    done = False

    if (data.count_withdraw == 3):
        print('''
Você atingiu o limite de saques de hoje.
        ''')
        done = True

    while not done:
        try:
            value = input('Valor do saque: ')

            if value == 'C' or value == 'c':
                done = True

            value = float(value)

            if (value < 0):
                print('''
O valor do saque não pode ser negativo.
                ''')
                raise ValueError()

            if (value > data.balance):
                print('''
O valor do saque é maior que o saldo disponível.
Verifique o saldo e tente novamente.
                ''')
                break
            
            data.balance = (data.balance - value)

            data.extract.append({
                'operation': 'Saque',
                'value': locale.currency(value),
            })

            done = True
            data.count_withdraw += 1

        except:
            print('''
Ocorreu um erro ao efetuar o saque.
Verifique se você inseriu um valor válido e tente novamente.
                  
Para cancelar o depósito, pressione [C].
            ''')