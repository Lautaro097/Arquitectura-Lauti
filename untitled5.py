pedirle al usuario  que me ingrese dos valores a y b, donde a me tome el valor de b y b me tome el valor de a
a = input("ingresar el valor de a: ")
b = input("ingresar el valor de b: ")
print(f"antes del intercambio: a = (a), b = (b)")
a, b = b, a
print(f"Despues del intercambio: a = (a), b = (b)")