def nums(x):
    if x == 0:
        return 'ноль'


    units = ['', 'один', 'два', 'три', 'четыре',
            'пять', 'шесть', 'семь', 'восемь', 'девять']


    units_case = ['', 'одна', 'две', 'три', 'четыре',
         'пять', 'шесть', 'семь', 'восемь', 'девять']


    doz = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
         'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']


    tens = ['', '', 'двадцать', 'тридцать', 'сорок',
         'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']


    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста',
         'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']


    thous = ['тысяча', 'тысячи', 'тысяч']


    millions = ['миллион', 'миллиона', 'миллионов']


    def three_digit(n):
        res = []
        hun = n // 100
        d = (n % 100) // 10
        u = n % 10
        if hun > 0:
            res.append(hundreds[hun])
        if d == 1:
            res.append(doz[u])
        else:
            if d > 1:
                res.append(tens[d])
            if u > 0:
                res.append(units[u])
        return ' '.join(res)

    def three_digit_case(n):
        res = []
        hun = n // 100
        d = (n % 100) // 10
        u = n % 10
        if hun > 0:
            res.append(hundreds[hun])
        if d == 1:
            res.append(doz[u])
        else:
            if d > 1:
                res.append(tens[d])
            if u > 0:
                res.append(units_case[u])
        return ' '.join(res)

    def cases_thousands(n):
        if n % 10 == 1 and n % 100 != 11:
            return thous[0]
        elif 2 <= n % 10 <= 4 and (n % 100 < 12 or n % 100 > 14):
            return thous[1]
        else:
            return thous[2]

    def cases_millions(n):
        if n % 10 == 1 and n % 100 != 11:
            return millions[0]
        elif 2 <= n%10 <= 4 and (n % 100 < 12 or n % 100 > 14):
            return millions[1]
        else:
            return millions[2]

    result=[]

    mil = x // 1000000
    th = (x % 1000000) // 1000
    un = x % 1000

    if mil > 0:
        mil_1 = three_digit(mil)
        if mil_1:
            result.append(mil_1)
            result.append(cases_millions(mil))

    if th > 0:
        th_1 = three_digit_case(th)
        if th_1:
            result.append(th_1)
            result.append(cases_thousands(th))

    if un > 0:
        un_1 = three_digit(un)
        if un_1:
            result.append(un_1)

    return ' '.join(result)


n_end=int(input())
print(nums(n_end))
