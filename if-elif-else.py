print("Ingrese un numero: ")
num = int(input())
print("Ingrese un numero: ")
num2 = int(input())
print("Ingrese un numero: ")
num3 = int(input())

print(num ,"/", num2 ,"/", num3)

if num>num2 and num>num3:
    print (num, "Es el digito mas grande")
elif num2>num and num2>num3:
    print(num2, "Es el digito mas grande")
else:
    print(num3, "Es el mas grande")