from random import choice

from utilities import int_range

def punkt_strich():
    p = choice(int_range(2,11))
    q = choice(int_range(2,11))
    a = choice(int_range(1,51))
    b = choice(int_range(1,51))

    produkt = p*q
    summe = a+b

    case1 = f"{p} \\cdot {q} = \\, ?"
    case2 = f"{produkt} : {p} = \\, ?"
    case3 = f"{a} + {b} = \\, ?"
    case4 = f"{summe} - {a} = \\, ?"

    V = choice(int_range(1,4))

    if V==1:
        question = case1
        answer = produkt
    elif V==2:
        question = case2
        answer = q
    elif V==3:
        question = case3
        answer = summe
    else:
        question = case4
        answer = b
    return question, answer