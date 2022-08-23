valor = float(input())
valor += 0.001
if 0 <= valor <= 1000000.00:
    x = valor // 100
    print('NOTAS:\n{} nota(s) de R$ 100.00'.format(int(x)))
    y = valor % 100
    x = y // 50
    print('{} nota(s) de R$ 50.00'.format(int(x)))
    y = y % 50
    x = y // 20
    print('{} nota(s) de R$ 20.00'.format(int(x)))
    y = y % 20
    x = y // 10
    print('{} nota(s) de R$ 10.00'.format(int(x)))
    y = y % 10
    x = y // 5
    print('{} nota(s) de R$ 5.00'.format(int(x)))
    y = y % 5
    x = y // 2
    print('{} nota(s) de R$ 2.00'.format(int(x)))
    print('MOEDAS:')
    y = y % 2
    x = y // 1
    print('{} moeda(s) de R$ 1.00'.format(int(x)))
    y = y % 1
    x = y // 0.50
    print('{} moeda(s) de R$ 0.50'.format(int(x)))
    y = y % 0.50
    x = y // 0.25
    print('{} moeda(s) de R$ 0.25'.format(int(x)))
    y = y % 0.25
    x = y // 0.10
    print('{} moeda(s) de R$ 0.10'.format(int(x)))
    y = y % 0.10
    x = y // 0.05
    print('{} moeda(s) de R$ 0.05'.format(int(x)))
    y = y % 0.05
    x = y // 0.01
    print('{} moeda(s) de R$ 0.01'.format(int(x)))