#! python
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

print(sorted(valores))
print(valores)

# valores.sort() --> mutável
# print(valores) --> mutável
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))
print(valores)

# valores.reverse() --> mutável
# print(valores) --> mutável