import os.path


def admiral(filename):
    notes_list = []
    path = os.path.join(os.path.dirname(__file__))
    if filename in os.listdir(path):
        msg = input('[+] Запись капитана: ')
        time = input('[+] Дата и время: ')
        notes_list.append(msg)
        notes_list.append(time)
        with open(f'{path}/{filename}', 'a') as file:
            file.write(f'{notes_list[0]} - {notes_list[1]} \n')

admiral('dnevnik')
