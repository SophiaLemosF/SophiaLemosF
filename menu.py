while True:
    print("========================")
    print("     Exercícios         ")
    print("========================")
    print("[1] - Exercicio de print")
    print("[2] - Exercicio de soma")
    print("[3] - Exercicio de conversão")
    print("[0] - Sair")
    print(" ")
    print("escolha:        ")
    x = input()
    if not x.isdigit():
        print("Digite apenas números!")
    else:
        x = int(x)
        if x == 2:
            print('Vc escolheu 2')
            mensagem = input("Coloque um número aqui: ")
            if not mensagem.isdigit():
                print("Digite apenas números!")
            else:
                print("Para realizar a soma, pegamos o número que você colocou e podemos somá-lo por qualquer número, neste caso iremos somar por 2")
                mensagem1 = int(mensagem)
                soma = mensagem1 + 2
                print("O resultado da soma será %s" % (soma))
            input("\n Aperte qualquer tecla para voltar.....")
        if x == 3:
            print('Vc escolheu 3')
            mensagem = input("Coloque algum número em metros aqui: ")
            if not mensagem.isdigit():
                print("Digite apenas números!")
            else:
                print("Temos %s metros" % (mensagem))
                print("Para realizar a conversão para centímetros multiplicamos o número que você colocou por 100")
                mensagem1 = int(mensagem)
                conversao = mensagem1 * 100
                print("Você terá %s centímetros" % (conversao))
            input("\n Aperte qualquer tecla para voltar.....")
        if x == 1:
            print('Vc escolheu 1')
            mensagem = input("Escreva alguma frase ou palavra aqui: ")
            print("Você escreveu {} \n".format(mensagem))
            print("Para que sua frase apareça na tela é preciso escrever print com as aspas assim --> print(),dentro dos parênteses com aspas, colocar sua frase e dar ENTER.")
            input("\n Aperte qualquer tecla para voltar.....")
        if x == 0:
            break
