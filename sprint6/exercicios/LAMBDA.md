## 3. Lab AWS Lambda
**Etapa 1 - Criar a função do *Lambda*:**  
<img src="../evidencias/lab-aws-lambda/criando-funcao.png" alt="print">

**Etapa 2 - Construir o código:**
* *Deploy* no *script lambda_function.py*:  
<img src="../evidencias/lab-aws-lambda/script-function.png" alt="print">  

* Erro de teste:  
<img src="../evidencias/lab-aws-lambda/erro-teste.png" alt="print">  

**Etapa 3 - Criar uma *layer*:**  
* *Build* do *Dockerfile*:  
<img src="../evidencias/lab-aws-lambda/buildando-imagem.png" alt="print">  

* ***Script* do *Dockerfile* para conferência:**
```Dockerfile
# Versão do Amazon Linux e Python foram alteradas por motivos de incompatibilidade. Comando 'pip install --upgrade pip' foi removido por ser inconsistente com o script deste Dockerfile.

FROM amazonlinux:2023.4.20240528.0
RUN yum update -y
RUN yum install -y \
    python3-pip \
    zip 
RUN yum -y clean all
RUN python3.9
```
* Rodando *container*, instalando o *Pandas* e compactando pasta:  
<img src="../evidencias/lab-aws-lambda/instalando-pandas.png" alt="print">  

* Copiando o *.zip* do *container* para a máquina local:  
<img src="../evidencias/lab-aws-lambda/copiando-layer.png" alt="print">  

* *Upload* do *layer* em um *bucket* no S3:  
<img src="../evidencias/lab-aws-lambda/upload-s3.png" alt="print">  

* Criando camada:  
<img src="../evidencias/lab-aws-lambda/config-layer.png" alt="print">  

**Etapa 4 - Utilizando a *layer*:**
* Adicionando *layer* à função *Lambda*:  
<img src="../evidencias/lab-aws-lambda/adicionando-layer.png" alt="print">  

* Configurando memória/tempo limite de execução do *script*:  
<img src="../evidencias/lab-aws-lambda/config-memoria.png" alt="print">  

* Execução final do *Lambda*:  
<img src="../evidencias/lab-aws-lambda/executando.png" alt="print">  

**Limpeza de recursos utilizados nos *labs*:**  
<img src="../evidencias/lab-aws-lambda/excluindo-bucket1.png" alt="print">  
<img src="../evidencias/lab-aws-lambda/excluindo-bucket2.png" alt="print"> 