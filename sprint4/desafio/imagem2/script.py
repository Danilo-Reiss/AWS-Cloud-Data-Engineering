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
