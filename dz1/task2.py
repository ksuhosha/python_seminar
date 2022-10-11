# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('X', 'Y', 'Z', '¬(X ⋁ Y ⋁ Z) ¬X ⋀ ¬Y ⋀ ¬Z', sep='\t')
for n in range(8):
    num = bin(n)
    num = num.replace('b', '0')
    X = int(num[-3])
    Y = int(num[-2])
    Z = int(num[-1])
    left_part = not (X or Y or Z)
    right_part = (not X) and (not Y) and (not Z)
    print(X, Y, Z, sep='\t', end='\t    ')
    print(left_part, sep='\t', end='\t    ')
    print(right_part, sep='\t', end='\t    ')
    print()
