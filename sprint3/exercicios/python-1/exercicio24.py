""" Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e 
ordenacaoDecrescente. Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] 
e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].
Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente. """


class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        crescente = sorted(self.listaBaguncada)
        return crescente

    def ordenacaoDecrescente(self):
        decresc = sorted(self.listaBaguncada)
        decresc.reverse()
        return decresc


crescente = [3, 4, 2, 1, 5]
crescente = Ordenadora(crescente)
print(crescente.ordenacaoCrescente())

decrescente = [9, 7, 6, 8]
decrescente = Ordenadora(decrescente)
print(decrescente.ordenacaoDecrescente())
