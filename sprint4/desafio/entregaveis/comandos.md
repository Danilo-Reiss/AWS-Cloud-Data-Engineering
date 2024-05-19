# Comandos utilizados no desafio:  
**Etapa 1:** 
  1. ```docker build -t imagem_desafio .``` --> Monta a imagem contida no Dockerfile do diretório atual sob o nome "imagem_desafio";
  2. ```docker run --name container_desafio imagem_desafio``` --> Cria um container chamado "container_desafio" com a imagem criada anteriormente.  
  
**Etapa 2:**  
  1. ``docker ps -a`` --> Lista todos os containers, parados e em execução;
  2. ``docker start -i container_desafio`` --> Roda novamente o container da etapa anterior em modo interativo.
  
**Etapa 3:**  
  1. ``docker build -t mascarar_dados .`` --> Monta a imagem com o novo Dockerfile indicando o CMD para o novo script Python.
  2. ``docker run -it --name container_mascarar_dados mascarar_dados`` --> Cria um container em modo interativo com a imagem que por sua vez, roda o script de conversão de strings em hash SHA-1 via input em loop infinito.
  3. ``Ctrl + D`` --> Sai do container

