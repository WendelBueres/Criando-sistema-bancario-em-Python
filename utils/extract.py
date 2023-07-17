import data
import locale

def extract():
    registro = 1

    print('-------------- Extrato --------------')

    if data.extract == []:
        print('''
Não foram realizadas operações.
        ''')
    
    for operation in data.extract:
        print(f'''
Registro: {registro}
Operação: {operation['operation']}
Valor: {operation['value']}
        ''')



        registro += 1

    if data.extract != []:
        print(f'''
-------------------------------------
Saldo da conta: {format(locale.currency(data.balance))}

*** Fim do Extrato ***
        ''')
    