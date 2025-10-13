#!/usr/bin/env python3

import sys               #importa o módulo sys, para receber os valores diretamente da linha de comando.

if len(sys.argv) != 8:   #usamos a condição para verificar se o usuário forneceu os 7 dados necessários (o primeiro valor da lista sys é o próprio nome do script, por isso são 8 elementos).
    print("Número incorreto de argumentos.")
    print("Uso correto: ./script_cDNA <DNA> <n1> <n2> <n3> <n4> <n5> <n6>")
    sys.exit(1)          #encerra o programa e o usuário deve recomeçar.

#Se o usuário forneceu o número correto de argumentos, o código segue normalmente.

dna = sys.argv[1]        #atribuímos o primeiro valor da linha de comando à variável 'dna'.
nums = sys.argv[2:]      #lista de 6 strings que devem ser convertidos para int.

if not all(n.isdigit() for n in nums):   #'.isdigit' verifica se os argumentos são numerais e o loop 'for' faz com que todos os elementos 'n' da lista 'nums' sejam verificados. Caso haja alguma divergência, o 'if not' é atendido e aparece a mensagem de erro.
    print("Erro: os argumentos n1 a n6 devem ser números inteiros positivos.")
    sys.exit(1)          #encerra o programa e o usuário deve recomeçar.

#Se todos os argumentos são compostos apenas por numerais, como verificamos, o código segue normalmente.

n1, n2, n3, n4, n5, n6 = [int(n) for n in nums]   #usamos "list comprehension" para transformar todos os elementos da lista 'nums' em inteiros.

DNA = dna.upper() #usamos o método '.upper()' para tornar todo o texto maiúsculo, caso o usuário tenha fornecido algum caractere minúsculo.

for base in DNA:         #usamos o loop 'for' para percorrer cada caractere da string da nova variável DNA
    if base not in "ATCG":
        print(f"Erro: a sequência contém caractere inválido: '{base}'")
        print("A sequência deve conter apenas A, T, C e G.")
        sys.exit(1)      #encerra o programa e o usuário deve recomeçar.

#Se a sequência de DNA é válida, continuamos.

pb = len(DNA)            #atribuímos a uma variável o número de pares de base que compõem a sequência de DNA.
indices = [n1, n2, n3, n4, n5, n6]       #criamos uma lista com os valores inteiros que correspondem às posições na sequência de DNA.

if any((n < 1 or n > pb) for n in indices):          #agora verificamos se todas as posições indicadas em 'indices' são válidas, ou seja, não são menores que 1 e nem maiores que o comprimento total da sequência.
    print(f"Erro: todos os índices devem estar entre 1 e {pb} (tamanho da sequência).")
    sys.exit(1)         #encerra o programa porque os índices são inválidos e o usuário deve recomeçar.

if not (n1 < n2 < n3 < n4 < n5 < n6):    #aqui verificamos se os índices estão estritamente ordenados em ordem crescente, visto que é importante que eles estejam em ordem para corresponderem ao intervalo correto da sequência de DNA. É impossível que n1 não seja o menor valor (primeiro número da sequência de DNA) e n6 não seja o maior.
    print("Erro: os índices devem obedecer a ordem n1 < n2 < n3 < n4 < n5 < n6.")
    sys.exit(1)        #também encerra o programa.

#Se os índices estão dentro do esperado, o programa continua.

CDS1 = DNA[n1 : n2]    #agora vamos atribuir cada parte da sequência a uma variável.
intron1 = DNA[n2 : n3 -1]
CDS2 = DNA[n3 : n4]
intron2 = DNA[n4 : n5 -1]
CDS3 = DNA[n5 : n6]

val1 = (len(intron1) >= 4) and (intron1.startswith("GT") and intron1.endswith("AG"))   #verificamos se cada íntron tem pelo menos 4 pares de base (o mínimo para cumprir as condições) e se inciam e terminam com os códigos indicados.

val2 = (len(intron2) >= 4) and (intron2.startswith("GT") and intron2.endswith("AG"))

if not val1:             #se não atender às condições da verificação, são impressos os erros que explicam os motivos pelos quais os íntrons são inválidos.
    print("Intron1 inválido: deve começar com 'GT' e terminar com 'AG'.")
    if len(intron1) < 4:
        print(f"  -> Intron1 muito curto (comprimento = {len(intron1)}).")
    else:
        print(f"  -> Intron1='{intron1}' não segue o padrão GT...AG.")
if not val2:
    print("Intron2 inválido: deve começar com 'GT' e terminar com 'AG'.")
    if len(intron2) < 4:
        print(f"  -> Intron2 muito curto (comprimento = {len(intron2)}).")
    else:
        print(f"  -> Intron2='{intron2}' não segue o padrão GT...AG.")

if val1 and val2:          #se atende aos critérios de val1 e val2, o código continua.
    print("Ambos os introns são válidos")
    cds = CDS1 + CDS2 + CDS3
    print(f"CDS1 + CDS2 + CDS3:\n{cds}")    #imprime apenas o CDS determinado pelos índices de forma concatenada.

else:
    print("\nNão foi possível montar a sequência final porque um ou ambos os introns são inválidos.")
    sys.exit(1)         #encerra o programa e o usuário deve recomeçar.
