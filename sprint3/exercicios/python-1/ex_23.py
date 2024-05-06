""" Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois 
(resultados negativos são permitidos). Utilize os valores abaixo para testar seu exercício:
x = 4 
y = 5
imprima:
Somando: 4+5 = 9
Subtraindo: 4-5 = -1 """


class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def somar(self):
        soma = self.x + self.y
        print(f'Somando: {self.x}+{self.y} = {soma}')

    def subtrair(self):
        sub = self.x - self.y
        print(f'Subtraindo: {self.x}+{self.y} = {sub}')


operation = Calculo(4, 5)
operation.somar()
operation.subtrair()
