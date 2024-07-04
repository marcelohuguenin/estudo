a = int(input ("Digite o valor para A: "))
while (a != 0):
    b = int(input ("Digite o valor para B: "))
    c = int(input ("1 para somar, 2 para subtrair, 3 para multipicar ou 4 para dividir: "))
    if (c == 1):
        resultado =int(a+b)
        print ("a soma de", a, "com", b, "é igual a:", resultado)
    elif (c == 2):
        resultado =int(a-b)
        print ("a subitração de", a, "com", b, "é igual a:", resultado)
    elif (c == 3):
        resultado = a*b
        print ("a multiplicação de", a, "com", b, "é igual a:", resultado)
    elif (c == 4):
        if (b == 0):
            print ("Divisão por zero não permitida")
        else:
            resultado = float(a/b)
            print ("a divisão de", a, "com", b, "é igual a:", resultado)
    else:
        print ("Opção Inválida.")
    a = int(input ("Digite o valor para A: "))