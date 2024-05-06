""" Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir:
Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu """


class Passaro:
    def voar(self):
        print('Animal\nVoando...')

    def emitir_som(self):
        print('Animal emitindo som...')


class Pato(Passaro):
    def voar(self):
        print('Pato\nVoando...')

    def emitir_som(self):
        print('Pato emitindo som...\nQuack Quack')


class Pardal(Passaro):
    def voar(self):
        print('Pardal\nVoando...')

    def emitir_som(self):
        print('Pardal emitindo som...\nPiu Piu')


def main():
    pato = Pato()
    pato.voar()
    pato.emitir_som()

    pardal = Pardal()
    pardal.voar()
    pardal.emitir_som()


main()
