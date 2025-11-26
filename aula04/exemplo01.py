#Verifica maior idade
# idade = int(input('Informe sua idade '))

# if idade >= 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade')


# Testando mais condições
# Teste de pontos

# pontos = int(input('Quantos pontos você fez? '))

# if pontos >= 100:
#     print('Nível máximo!')
# elif pontos >= 50:
#     print('Nível bom!')
# elif pontos >= 25:
#     print('Pode melhorar!')
# else: 
#     print('Pontuação Baixa...')


# Verificação de login
# usuario = input('Informe o usuário: '). lower()
# senha = input('Digite a senha ')

# if usuario == 'admin' and senha =='1234':
#     print(f'Bem-vindo {usuario}!')
# else:
#     print('Usuário ou senha incorreto')

#Condição para brinde
# compra = float(input('Digite o valor da compra: '))
# frequencia = input('Cliente Frequente?[S/N] '). lower()

# if compra>= 1000 or frequencia == 's':
#     print('Parabéns, você ganhou um brinde!')
# else:
#     print('Sem brinde!')


#Exemplo com nota e frequencia

nota = float(input('Informe sua nota: '))
frequencia = float(input('Informe sua frequencia: '))

if nota >= 7:
    if frequencia >= 75:
        print ('Parabéns, voê está aprovado!')
    else:
        print('Boa nota, mas o aluno foi reprovado por falta!')
else: 
    print('Reprovado por nota abaixo da média!')