nome, salario_fixo, total_vendas = input(), float(input()), float(input())
real = total_vendas * 0.15
novo = salario_fixo + real
print('TOTAL = R$ %.2f' %novo)