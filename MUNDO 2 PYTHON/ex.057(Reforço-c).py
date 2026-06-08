estado_civil = str(input('Digite sua estado civil:[C/S/D/V] ')).upper().strip()[0]
while estado_civil not in 'CSDV':
    print(f'Estado Civil:{estado_civil}, invalido digite novamente')
    estado_civil = str(input('Digite sua estado civil:[C/S/D/V] ')).upper().strip()[0]
if estado_civil == 'S':
        extenso = 'Solteiro(a)'
elif estado_civil == 'C':
        extenso = 'Casado(a)'
elif estado_civil == 'D':
        extenso = 'Divorciado(a)'
else:
        extenso = 'Viúvo(a)'
print(f'Estado Civil:{extenso},cadastrado com sucesso')