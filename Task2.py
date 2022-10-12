#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('X'))

y = int(input('Y'))

z = int(input('Z'))
if not(x or y or z) == (not x) and (not y) and (not z):
    print('True')
else:
    print('False')