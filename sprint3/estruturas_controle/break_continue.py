for x in range(1, 11): 
    if x % 2 == 0:
        continue # --> Vai para próxima iteração
    print(x)

for x in range(1, 11):
    if x == 5:
        break # --> Interrompe o laço
    print(x)

print('Fim!')