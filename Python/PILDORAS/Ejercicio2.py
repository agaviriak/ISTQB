#programa con condicionales
print("VALIDACION DE NOTAS")
notaF= float(input("Digite Nota Final: "))

def validacion(nota):
	if nota<3:
		estado="reprobado"
	else:
		estado="Aprobado"
	return estado

print(validacion(notaF))


