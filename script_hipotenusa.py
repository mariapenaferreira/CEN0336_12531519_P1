#!/usr/bin/env python3 
#esse comando permite que o script seja executado automaticamente, sem a necessidade de digitar o interpretador

#Para dois números inteiros positivos a e b, cada um menor que 500, calcule o inteiro que corresponde ao quadrado da hipotenusa do triangulo retângulo que tem lados com tamanho a e b.

import sys                 #importa o módulo sys, para receber os valores da linha de comando

if len(sys.argv) != 3:     #aqui vamos verificar se o usuário usou corretamente o módulo sys, colocando o nome do script seguido por exatamente dois números (ou seja, o número de argumentos não pode ser diferente (!=) de 3);
	print("Erro: você deve fornecer exatamente dois números inteiros, positivos, menores que 500 e que correspondam ao valor dos catetos.")
	print("Uso: python3 script_hipotenusa.py <a> <b>")     #aqui mostramos para o usuário a formatação esperada para o envio dos dados;
	sys.exit(1)  #encerra o programa com código de erro;
else:                #caso não seja encontrado esse primeiro erro, o programa continua;


	a_string = sys.argv[1]     #as variáveis ganharam os nomes seguidos de _string porque depois será necessário convertê-las para inteiro, ainda são strings;
	b_string = sys.argv[2]     #aqui atribuímos os valores digitados na linha de comando pelo usuário a duas variáveis;

	if not (a_string.isdigit() and b_string.isdigit()):                  #aqui o método .isdigit é usado para conferir se os argumentos são de fato números inteiros (ele verifica se são apenas numerais na string, retornando falso para a presença de pontos, hífen ou letras);
		print("Erro: os valores inseridos devem ser números inteiros e positivos")
		sys.exit(1)        #encerra o programa com código de erro e o usuário precisa recomeçar;
	else:                      #sem esse segundo erro, o programa segue para uma próxima verificação;

		a = int(a_string)
		b = int(b_string)          #convertemos as variáveis de string para o formato inteiro;

		if a == 0 or b == 0:       #verifica se algum dos valores indicados pelo usuário indica um lado de comprimento igual a zero (não existe);
    			print("Erro: Nenhum dos valores pode ser igual a zero.")
    			sys.exit(1)
		else:              #sem essa terceira possibilidade de erro do usuário, o programa continua;
		
			if a >= 500 or b >= 500:   #verificamos se os valores que o usuário forneceu estão dentro do especificado;
				print("Erro: os valores fornecidos devem ser inferiores a 500.")
				sys.exit(1)        #encerra o programa com código de erro;
			else:                      #novamente, não havendo erro o programa pode finalizar a operação;

				hipo_quadrada = a**2 + b**2       #a operação de potenciação é representada pela base seguida por dois asteríscos e o valor do expoente;
				print("O quadrado da hipotenusa para o triangulo retângulo com lados a={} e b={}, é {}.".format(a, b, hipo_quadrada))

