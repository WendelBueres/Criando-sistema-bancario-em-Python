def check_operation (operacao):
    is_valid = False

    while not is_valid:
        try:
            operacao = int(operacao)

            if operacao > 5 or operacao < 1: 
                raise ValueError()
            is_valid = True

            return operacao
        except:
            if operacao == 'H' or operacao == 'h':
                print('''
Selecione uma operação:
[1] Depósito
[2] Saldo
[3] Saque
[4] Extrato
[5] Sair
                ''')
            else:
                print('''
Operação inválida.
Pressione [H] para listar as operações.
                ''')
                
            operacao = input('Operação: ')