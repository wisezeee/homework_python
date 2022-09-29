import os.path


def admiral(filename):
    path = os.path.join(os.path.dirname(__file__))
    if filename in os.listdir(path):
        msg = input('[+] Запись капитана: ')
        time = input('[+] Дата и время: ')
        with open(f'{path}/{filename}', 'a') as file:
            file.write(f'{time} - {msg} \n')
            file.close()
    else:
        with open(f'{path}/{filename}', 'w') as file:
            file.close()
        return admiral(filename)


admiral('dnevnik')
