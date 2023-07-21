from utils import date_format, cpf_format
from data import users

def create_user(name, date_born, cpf, address):
    REQUIRED_FIELDS = [
        {"description": "nome", "value": name},
        {"description": "data de nascimento", "value": date_born},
        {"description": "CPF", "value": cpf},
        {"description": "endereço", "value": address},
    ]

    done = False
    error = False

    while not done:
        try:
            for field in REQUIRED_FIELDS:
                if not field["value"]:
                    print(f'\nO campo {field["description"]} é obrigatório.')

                    error = True
                
                if field["description"] == "endereço":
                    REQUIRED_FIELDS_ADDRESS = [
                        {"description": "logradouro", "value": address['logradouro']},
                        {"description": "numero", "value": address['numero']},
                        {"description": "bairro", "value": address['bairro']},
                        {"description": "cidade", "value": address['cidade']},
                        {"description": "estado", "value": address['estado']},
                    ]

                    for field_address in REQUIRED_FIELDS_ADDRESS:
                        if not field_address['value']:
                            print(f"\nO campo {field_address['description']} é obrigatório.")

                            error = True

            if error:
                raise ValueError()

            date_born = date_format(date_born)
            cpf = cpf_format(cpf)

            for user in users:
                if user['cpf'] == cpf:
                    print('\nJá existe um usuário com esse CPF.')

                    raise ValueError()
                
            user = {
                'id': len(users) + 1,
                'name': name,
                'date_born': date_born,
                'cpf': cpf,
                'address': address
            }

            users.append(user)

            print('Id do usuário:', user['id'])
            print('\nUsuário criado com sucesso.')

            done = True

        except:
            print('\nOcorreu um erro ao criar o usuário.')            

            done = True
            