a = 1
b = 1
c = 1
d = 1
e = 1


listas2 = ["a^b", "-a^b", "a^0", "-a^0", "a^0", "a/b^3", "a^-2", "a/b^-3", "((-a)^3)^4", "(0.a)^3", "(0.a)^4", "0^a", "a + (0.b)^c", "a/b + c^d - d^-b", "a^-b+(-c)-d", "(a/b - c/d + c)^d + c/(c+e^d-(a-b)^-d)"]
contador = 0
while True:
    if contador > len(listas2) -1:
        break
    print("Questão ", contador+1)
    print(listas2[contador])
    
    if listas2[contador].find('a') != -1:
        print("Qual o valor de a?")
        a = float(input("VALOR: "))
    if listas2[contador].find("b") != -1:
        print("Qual o valor de b?")
        b = float(input("VALOR: "))
    if listas2[contador].find("c") != -1:
        print("Qual o valor de c?")
        c = float(input("VALOR: "))
    if listas2[contador].find("d") != -1:
        print("Qual o valor de d?")
        d = float(input("VALOR: "))
    if listas2[contador].find("e") != -1:
        print("Qual o valor de e?")
        e = float(input("VALOR: "))
    

    #listas2 = ["a^b", "-a^b", "a^0", "-a^0", "a^0", "a/b^3", "a^-2", "(a/b)^-3", "((-a)^3)^4", "(aF)^3", "(0.a)^4", "0^a", "a + (0.b)^c", "a/b + c^d - d^-b", "a^-b+(-c)-d", "(a/b - c/d + c)^d + c/(c+e^d-(a-b)^-d)"]
    listas = [
        (a**b), 
        (pow(-a,b)), 
        (a**0), 
        (pow(-a,0)), 
        (a**0), 
        ((a/b)**3), 
        (a**-2), 
        ((a/b)**-3), 
        (((-a)**3)**4), 
        (a**3), 
        ((a)**4), 
        0, 
        (a + (b)**c), 
        ((a/b)+c**d-d**(-b)),
        (a**(-b) + (-c**(-5))),
        (((a/b - c/d + c)**(-d))+ c/(c+e**d-(a-b)**(-d)))
        ]
    print("Resultado: ", listas[contador])
    print("----------\n\n")
    contador += 1
