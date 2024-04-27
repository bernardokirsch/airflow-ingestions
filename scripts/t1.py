from functions import soma, subtracao

def resultado():
    resultado = []

    resultado_soma = soma(5, 3)
    resultado_subtracao = subtracao(10, 4)

    print("t1 - soma:", resultado_soma)
    print("t1 - subtração:", resultado_subtracao)

    resultado.append(resultado_soma)
    resultado.append(resultado_subtracao)

    with open('/tmp/resultado.txt', 'w') as f:
        for item in resultado:
            f.write("%s\n" % item)

resultado()