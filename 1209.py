def count(lay):
    small = 0
    large = 0
    for i in lay:
        if i.islower():
            small += 1
        elif i.isupper():
            large += 1
    if large > small:
        return 1
    elif large < small:
        return -1


def allStr(mas):
    counter = 0
    for i in (mas):
        y = count(i)
        if y == 1:
            counter += 1
    print('Заглавных больше у ' + str(counter / len(mas) * 100) + '% строк')


x = str(input())
mas = x.split()
allStr(mas)
