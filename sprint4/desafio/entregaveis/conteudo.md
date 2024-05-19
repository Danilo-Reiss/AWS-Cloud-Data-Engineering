## Conteúdo do script Python, Dockerfile e comando de inicialização de container da etapa 3:
**Script Python:**
```python
import hashlib


def sha1_hash(input):
    # Instancia um objeto de hash SHA-1
    sha1 = hashlib.sha1()

    # Atualiza o objeto com o input convertido em bytes usando codificação UTF-8
    sha1.update(input.encode('utf-8'))

    # Obtém o valor hexadecimal através do método hexdigest
    hash_hex = sha1.hexdigest()

    return hash_hex

while True:
    string = str(input('Digite uma string: '))
    hex_result = sha1_hash(string)

    print(f"A string '{string}' tem como hash SHA-1 '{hex_result}'")
```

**Dockerfile:**
```dockerfile
FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "script.py" ]
```

**Comando de inicialização no terminal:**
```terminal
docker build -t mascarar_dados .
docker run -it --name container_mascarar_dados mascarar_dados
```