n1 = int (input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
menor = n1
if n2 < n1 and n2 < n3:
    nenor = n2
if n3 < n1 and n3 < n2:
    menor = n3
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2 
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número é {maior} e o menor número é {menor}')
#fim

