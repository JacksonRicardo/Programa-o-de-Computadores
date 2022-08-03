numero_funcionario, horas_trabalhadas, resultado = int(input()), float(input()), float(input())
salario = horas_trabalhadas*resultado
s = "{:.2f}".format(salario)
print("NUMBER =", numero_funcionario)
print("SALARY = U$",s)
