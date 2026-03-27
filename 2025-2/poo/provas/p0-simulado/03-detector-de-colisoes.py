# Leitura dos valores dos dois retângulos
ax1, ay1, ax2, ay2 = [int(w) for w in input().split()] # A
bx1, by1, bx2, by2 = [int(w) for w in input().split()] # B

# Verificar se NÃO HÁ interseção
if (ax2 < bx1) or (bx2 < ax1) or (ay2 < by1) or (by2 < ay1):
    print(0)
else:
    print(1)