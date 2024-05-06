""" Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) 
e um atributo público de nome id. Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro 
para retornar o valor do respectivo atributo. Lembre-se que o acesso ao atributo privado deve ocorrer somente através 
dos métodos definidos, nunca diretamente. Você pode alcançar este comportamento através do recurso de properties do Python. """


class Pessoa:
    def __init__(self, id):
        self.__nome = None
        self.id = id

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    nome = property(get_nome, set_nome)


p = Pessoa(0)
p.nome = 'Fulano de Tal'
print(p.nome)
