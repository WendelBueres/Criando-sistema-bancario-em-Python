import data
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def deposit():
    done = False

    while not done:
        try:
            value = input('value do depósito: ')

            if value == 'C' or value == 'c':
                done = True

            value = float(value)

            if (value < 0):
                print('''
O valor do depósito não pode ser negativo.
                ''')
                raise ValueError()
            
            data.balance = (data.balance + value)

            data.extract.append({
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
