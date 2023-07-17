from utils.check_operation import check_operation
from utils.deposit import deposit
from utils.balance import balance
from utils.withdraw import withdraw
from utils.extract import extract


if __name__ == '__main__':
    done = False
    operation = 0

    while not done:
      print('''
Selecione uma operação:
  [1] Depósito
  [2] Saldo
  [3] Saque
  [4] Extrato
  [5] Sair
      ''')
      operacao = input('Operação: ')

      operacao = check_operation(operacao)

      if (operacao == 1):
        deposit()

      elif (operacao == 2):
        balance()

      elif (operacao == 3):
        withdraw()         

      elif (operacao == 4):
        extract()

      elif (operacao == 5):
        print('''
Sessão finalizada.
        ''')
        done = True

          