def count(lay):
    small = 0
    large = 0
    for i in lay:
        if i.islower():
            small += 1
        elif i.isupper():
            large += 1
    if large > small:
        return True
    elif large < small:
        return False


def allStr(mas):
    counter = 0
    for i in (mas):
        if count(i):
            counter += 1

    print('Заглавных букв больше у ' + str(counter / len(mas) * 100) + '% строк')


x = str(input())
mas = x.split()
allStr(mas)
