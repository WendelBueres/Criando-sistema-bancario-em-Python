import datetime

def date_format(date_born):
    if (date_born[2] == '/' or date_born[4] == '/'):
        date_born = date_born.split('/')
                
    elif (date_born[2] == '-' or date_born[4] == '-'):
        date_born = date_born.split('-')
                
    elif (date_born[2] == '.' or date_born[4] == '.'):
        date_born = date_born.split('.')

    elif (date_born[2] == ',' or date_born[4] == ','):
        date_born = date_born.split(',')

    try:
        date_born = datetime.date(int(date_born[2]), int(date_born[1]), int(date_born[0]))

        today = datetime.date.today()

        if (today.year - date_born.year) < 18:
            print('Para ser cliente do banco, é necessário ter mais de 18 anos.')
            raise ValueError()

        return date_born
    except:
        print('''
Data de nascimento inválida.
                ''')
        raise ValueError()
            
