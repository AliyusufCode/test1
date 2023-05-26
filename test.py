print('простой калькулятор')
x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))

y= input('Что будем делать(+,-,/,*): ')
if y == '+' :
    s1 = x1+x2
    print(s1)
elif y == '-':
    s2 = x1 - x2
    print(s2)
elif y == '/':
    s3 = x1/x2
    print(s3)
elif y == '*':
    s4 = x1*x2
    print(s4)
else:
    print('выбрали неверную операцию...')