import os.path
import datetime

def admiral(filename, date, notes):
    path = os.path.join(os.path.dirname(__file__))
    delta = datetime.timedelta(days=1)
    with open(f'{path}/{filename}', 'w') as file:
        note = 0
        while note < len(notes):
            file.write(date.strftime('%d.%m.%Y') + f': {notes[note]} \n')
            note += 1
            date += delta


date = datetime.date.today()
admiral('dnevnik', date, ['Сегодня убило 3 матроса', 'Сегодня поймали белую акулу, поели...'])


