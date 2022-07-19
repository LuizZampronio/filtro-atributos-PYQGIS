layer = iface.activeLayer()

atributos = layer.getFeatures()
nomeCampo = 'Area (ha)'
indiceCampo = layer.fields().indexOf(nomeCampo)

totalTalhoes = 0
total70 = 0

for atributo in atributos:

    totalTalhoes += 1

    maior70 = atributo.attributes()[indiceCampo]

    if maior70 > 70:
        print('Fazenda: {}'.format(atributo.attributes()[1]))
        print('Talhão: {}'.format(atributo.attributes()[0]))
        print('Área (ha): {}'.format(atributo.attributes()[indiceCampo]))
        print('\n')

        total70 += 1

print('\n')
print('Quantidade total de talhões {}'.format(totalTalhoes))
print('Quantidade total de selecionados {}'.format(total70))
