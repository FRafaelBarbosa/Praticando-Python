from math import sqrt, ceil, floor
import random
import emoji

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual {:.2f}'.format(num, ceil(raiz)))
print('A raiz de {} é igual {:.2f}'.format(num, floor(raiz)))

#random

num2 = random.randint(1, 10)
print(num2)