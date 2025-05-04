def montar_conexoes(transformadores, linhas, cargas):
    def barramento_base(bus):
        return bus.split('.')[0] if isinstance(bus, str) else bus

    conexoes = {}

    for tf in transformadores:
        conexoes[tf.nome] = {
            barramento_base(tf.bus_primario),
            barramento_base(tf.bus_secundario)
        }

    for linha in linhas:
        conexoes[linha.nome] = {
            barramento_base(linha.bus1),
            barramento_base(linha.bus2)
        }

    for carga in cargas:
        conexoes[carga.nome] = {barramento_base(carga.bus)}

    return conexoes


def ordenar_por_topologia(conexoes, origem='barra01'):
    visitados = set()
    ordem = []
    barramentos_para_visitar = [origem]

    while barramentos_para_visitar:
        atual = barramentos_para_visitar.pop(0)
        for elemento, barras in conexoes.items():
            if elemento in visitados:
                continue
            if atual in barras:
                ordem.append(elemento)
                visitados.add(elemento)
                barramentos_para_visitar.extend(barras - {atual})
    return ordem