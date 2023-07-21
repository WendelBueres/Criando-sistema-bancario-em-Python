def cpf_format(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    cpf = cpf.replace('/', '')

    if (len(cpf) != 11):
        print('CPF inválido. Tente novamente.')

        raise ValueError()
    
    return cpf