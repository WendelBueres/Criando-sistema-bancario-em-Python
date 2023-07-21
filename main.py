from utils.check_operation import check_operation
from operations.deposit import deposit
from operations.balance import balance
from operations.withdraw import withdraw
from operations.extract import extract
from operations.create_user import create_user
from operations.create_account import create_account

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
  [5] Criar novo usuário
  [6] Criar nova conta
  [7] Sair
      ''')
      operacao = input('Operação: ')

      operacao = check_operation(operacao)

      if (operacao == 1):
        deposit(account_id=input('Número da conta: '))

      elif (operacao == 2):
        balance(account_id=input('Número da conta: '))

      elif (operacao == 3):
        withdraw(account_id=input('Número da conta: '), value=input('Valor do saque: '))         

      elif (operacao == 4):
        extract(account_id=input('Número da conta: '))

      elif (operacao == 5):
        print('\nDigite os dados do usuário')
        name = input('Nome: ')
        date_born = input('Data de nascimento: ')
        cpf = input('CPF: ')
        print('\nDigite o Endereço')
        address = {
          'logradouro': input('Logradouro: '),
          'numero': input('Número: '),
          'bairro': input('Bairro: '),
          'cidade': input('Cidade: '),
          'estado': input('Estado: '),
        }

        create_user(name=name, date_born=date_born, cpf=cpf, address=address)

      elif (operacao == 6):
        create_account(input('Id do usuário: '))

      elif (operacao == 7):
        print('''
Sessão finalizada.
        ''')
        done = True

          