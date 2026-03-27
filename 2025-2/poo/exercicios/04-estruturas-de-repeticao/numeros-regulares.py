n = int(input("Digite um número: "))

if n <= 1:
    eh_regular = False
else:
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    eh_regular = (n == 1)
    
print(eh_regular)