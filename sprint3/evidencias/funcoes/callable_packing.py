#! python
def calc_preco_final(preco_bruto, calc_imposto, *params): # --> packing dos parâmetros da outra função
    return preco_bruto + preco_bruto * calc_imposto(*params) # --> unpacking dos parâmetros para a chamada da outra função



def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_brut = 134.98
    preco_final = calc_preco_final(preco_brut, imposto_x, True)     # --> Argumentos que servem como parâmetro da função imposto
    preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
    print(f'Preço final R$ {preco_final}')
