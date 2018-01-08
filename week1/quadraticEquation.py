import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b**2 - (4 * a * c)
print()

if D > 0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
elif D == 0:
    x1 = x2 = -b / (2 * a)
else:
    print("No roots among real number")

print(x1)
print(x2)
