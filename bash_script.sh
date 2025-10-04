#!/bin/bash
#essa linha indica qual programa vai executar o script (é como a que usamos para rodar os scripts em Python, permite que o script rode diretamente)

echo "Diretório atual:"                           #echo é o comando de scripts bash para imprimir (como o print em python);
pwd                                               #pwd mostra o caminho completo das pastas até o diretório em que se está;

ls -l -a /home/maria_eduarda > lista_HOME.TXT     #ls mostra o conteúdo de um diretório; -l mostra o formato longo, ou seja, mais detalhes de cada arquivo; -a significa all, ou seja, mostra até os aquivos ocultos; /home/maria_eduarda mostra qual é minha pasta atual e que a lista se refere aos arquivos presentes nela; > direciona a lista para o arquivo de texto;

echo "Data atual:"
date                                              #date mostra a data e hora atual (para que mostre apenas a data, sem a hora deveria ser <date + %d/%m/%Y>

