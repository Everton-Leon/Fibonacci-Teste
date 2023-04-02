# interface
print('--' * 20)
print(f'{"Sequencia de Fibonacci".center(30)}')
print('--' * 20)

# coletando dados do usuario
n = 1000
op = int(input('Qual termo você quer analizar?  '))
termo = False

# lógica
t1 = 0
t2 = 1
if op == t1 or op == t2:
    termo = True
#print(f'{t1} --> {t2}', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    #print(f' --> {t3}', end='')  # resposta
    t1 = t2
    t2 = t3
    if op == t3:
        termo = True
    cont += 1

# resposta
if termo:
    print(f'O número {op} existe na sequencia.')
else:
    print(f'O número {op} não existe na sequencia.')
