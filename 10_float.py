x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x==y)

# forma string
y_str = format(y, ".2g")
print(y_str)
print(y_str==str(x))

print('*'*10)
# forma matematica
print(x,y)
tolerancia = 0.00001
print(abs(x-y) < tolerancia)
