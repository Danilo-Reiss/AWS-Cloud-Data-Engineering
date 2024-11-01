def get_tipo_dia(dia):
    match dia:
        case 2 | 3 | 4 | 5 | 6:
            return 'Dia de semana'
        case 1 | 7:
            return 'Fim de semana'
        case _:
            return '** inválido **'


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_tipo_dia(day)}')
