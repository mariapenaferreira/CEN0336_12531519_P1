#!/usr/bin/env python3

seq = input('Cole aqui a sequência de DNA: ').upper()                      #criamos uma variável que recebe o valor através da função input. 
                                                                           #O método de string .upper() faz com que tudo fique em maiúsculo.

for base in seq:                                                           #O for vai percorrer a sequência toda e cada caractere será definido pela variável 'base';
    if base not in "ATCG":                                                 #Se 'base', ou seja, um dos caracteres, não pertencer à sequência 'ATCG', o código seguirá para a mensagem de erro;
        print("Erro: sequência contém caracteres inválidos.")
        quit()                                                             #Encerra o progrma;
    else:                                                                  #Não havendo problema na sequência, seguimos para a contagem;
        cont_A = 0
        cont_T = 0
        cont_C = 0
        cont_G = 0                                                         #Criamos 4 variáveis para armazenar o valor da contagem;

        for base in seq:                                                   #Novamente, usamos um looping for para percorrer toda a sequência de DNA;
            if base == 'A':
                cont_A += 1                                                #Se a base equivale a 'A', uma unidade é adicionada na variável de contagem de 'A', e assim por diante com as demais variáveis;
            elif base == 'T':
                cont_T += 1
            elif base == 'C':
                cont_C += 1
            elif base == 'G':
                cont_G += 1

#Por fim, através de um 'print' mostramos para o usuário o valor da contagem de cada nucleotídeo. A formatação \ n faz com que cada informação fique em uma linha.
print('A sequência inserida é composta por: \nA:{}\nT:{}\nC:{}\nG:{}'.format(cont_A, cont_T, cont_C, cont_G))
