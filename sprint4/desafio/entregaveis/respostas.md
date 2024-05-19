# Respostas para os questionamentos do desafio:
  
**1. É possível reutilizar containers?**  
**R:** Sim, é possível reutilizar containers já utilizados anteriormente.  
  
**2. Apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker.**  
**R:** Uma vez sabendo o ID ou nome do container, é possível reutilizá-lo seguindo a seguinte sintaxe:  
``docker start <NAME/ID_CONTAINER>``  
É possível também rodar o container de forma interativa utilizando a flag ``-i`` . 
  
**3. Não sendo possível reutilizar o container, justifique.**  
**R:** Não será possível reutilizar um container caso o mesmo seja configurado para rodar uma imagem e ser deletado após a execução através da flag ``--rm`` no comando ``docker run``.