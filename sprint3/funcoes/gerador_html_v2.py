#! python
def tag_bloco(texto, classe='success', inline=False): # --> Definindo o padrão de classe e inline
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True)) # --> Posicional
    print(tag_bloco('inline', inline=True)) 
    print(tag_bloco(inline=True, texto='inline')) # --> Nomeado
    print(tag_bloco('falhou', classe='error'))