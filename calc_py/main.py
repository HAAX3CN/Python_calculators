import operadores

expressao = input("")
interpretador = expressao.split()


def Operacao(n, op, n2):
    if(op == '+'):
        return operadores.Soma(n, n2)
    elif(op == '-'):
        return operadores.Subtracao(n, n2)
    elif(op =='*'):
        return operadores.Multiplicacao(n, n2)
    elif(op ==  '/'):
        if(n2 == 0):
            return print("Não pode dividir por zero!...")
        else:
            return operadores.Divisao(n, n2)
    return 0

def Program():
    if(len(interpretador)!=3):
        print("Expressão inválida! Tente Novamente!")
    else:
        n = float(interpretador[0])
        operacao = interpretador[1]
        n2 = float(interpretador[2])
        resultado = Operacao(n, operacao, n2)
        print(resultado)
Program()
