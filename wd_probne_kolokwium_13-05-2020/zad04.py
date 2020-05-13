# Zad 4
# gotowe

# def foo(n):
#     if(n == 1):
#         return 1
#     if(n == 0):
#         return 0
#     return foo(n-1) + foo(n-2)    # zostawiam w celach dydaktycznych

# def foo2(n):
#     wynik = []
#     for i in range(n):
#         wynik[i] = foo(i)     # ????
#     return wynik              # zostawiam w celach dydaktycznych

def foo3(n):
    wynik = [0,1]
    for i in range(n-2):
        wynik.append(wynik[i] + wynik[i+1]) 
    return wynik

a = 6
print(foo3(a))
