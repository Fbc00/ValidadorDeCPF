cpf_digitado = input('Digite seu CPF: ').replace(' ', '')

contador = 10
cpf_total = ''
for i in range(0, 2):
    aux = 0
    for key, valeu in enumerate(range(contador, 1, -1)):
        valor = int(cpf_digitado[key])
        aux += valor * valeu
    digito = 11 - (aux % 11)

    if digito > 9 : digito = 0

    if contador == 10:
        cpf_temp = cpf_digitado[:9] + str(digito)
    else:
        cpf_total = cpf_temp + str(digito)
    contador += 1
if cpf_total == cpf_digitado:
    print(cpf_total)
    print('seu cpf é válido')
else:
    print('CPF INVÁLIDO')