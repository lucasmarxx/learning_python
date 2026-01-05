# def criar_saudacao(saudacao):
#     def saudar(nome):
#        return f'{saudacao}, {nome}!' 
#     return saudar

# falar_bom_dia = criar_saudacao('bom dia')
# falar_boa_noite = criar_saudacao('boa noite')

# print(falar_bom_dia('Luquinhas'))
# print(falar_boa_noite('Luquinhas'))

# nomes = ['Dandan', 'Bibito', 'Luquinhas', 'Rafinha', 'Paolinha']
# for nome in nomes:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))


# def externa(a):
#     def interna(b):
#         return f'{a} e {b}'
    
#     return interna

# incompleto = externa('esse é o a')
# completo = incompleto('esse é o b')
# print(completo)

def multiplicador(multiplicador):
    def multiplicar(multiplica):
        return multiplicador * multiplica
    return multiplicar

multiplicador_input = int(input('Por quanto vc quer multiplicar??? '))
segundo_numero = int(input('vezes quanto? '))
# multiplica_multiplicador = int(input('E por quanto vc quer multiplicar este numero??? '))
primeiro_numero = multiplicador(multiplicador_input)
resultado = primeiro_numero(segundo_numero)
print(resultado)

multiplicador_2 = multiplicador(2)
multiplicador_3 = multiplicador(3)
multiplicador_4 = multiplicador(4)

print(multiplicador_2(5))
print(multiplicador_3(5))
print(multiplicador_4(5))

# def validador_menor_que(valor_minimo):
#     def e_menor(valor):
#         return valor < valor_minimo
#     return e_menor

# numero_flag = validador_menor_que(50)

# diga_numero = int(input('Digite um número: '))
# diga_numero2 = int(input('Digite outro número: '))

# teste_primeiro_numero = numero_flag(diga_numero)
# teste_segundo_numero = numero_flag(diga_numero2)

# print(f"60 < 50 ~ {teste_primeiro_numero}")
# print(f"30 < 50 ~ {teste_segundo_numero}")