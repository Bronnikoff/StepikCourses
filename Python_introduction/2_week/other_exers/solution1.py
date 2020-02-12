def gen_series(series):
    """
    генератор серий лотерейных билетов начиная с series по "ZZ" включительно, входные 
    параметры: series -  - номер серии, выход - строка, состоящая из двух заглавных 
    букв латинского алфавита
    """
    letter_1 = series[0].upper()
    letter_2 = series[1].upper()
    while letter_1 < 'Z' or letter_2 < 'Z':
        yield letter_1 + letter_2

        if letter_2 == 'Z':
            letter_2 = 'A'
            letter_1 = chr(ord(letter_1) + 1)
        else:
            letter_2 = chr(ord(letter_2) + 1)
    yield letter_1 + letter_2



def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры: 
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    for i in range(1, 10 ** length):
        yield f"%0{length}d" % i


def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    ser_gen = gen_series(series)
    i = 0
    while i < count:
        second = next(ser_gen)
        for first in gen_number(length):
            if i < count:
                yield first + " " + second
                i += 1
            else:
                break