#Solicitamos al usuario el numero
num = int(input("Por favor ingrese un numero entero: "))
digitos = 0

#Hacemos el valor absoluto del numero para admitir numeros negativos
num = abs(num)
while num > 0:
    num = num // 10
    digitos += 1
print(f"El numero ingresado tiene {digitos} digitos")
