class GeradorDSS:
    def __init__(self, transformadores, linhas, cargas, bases_tensao, ordem):
        self.transformadores = {tf.nome: tf for tf in transformadores}
        self.linhas = {l.nome: l for l in linhas}
        self.cargas = {c.nome: c for c in cargas}
        self.bases_tensao = bases_tensao
        self.ordem = ordem

    def gerar_codigo(self):
        dss = []

        # Cabeçalho do circuito
        dss.append("Clear")
        dss.append("New object=circuit.Exercicio_modelo bus1=barra01 basekv=34.5 phases=3 mvasc3=1000000")

        # Adiciona os elementos conforme a ordem definida
        for nome in self.ordem:
            if nome in self.transformadores:
                tf = self.transformadores[nome]
                dss.append(
                    f"New transformer.{tf.nome} phases=3 windings= {tf.windings} "
                    f"%loadloss={tf.loadloss}  %noloadloss={tf.noloadloss} XHL={tf.xhl}"
                )
                dss.append(
                    f"~ wdg=1 bus={tf.bus_primario} kv={tf.kv_primario} kVA={tf.kva}"
                )
                dss.append(
                    f"~ wdg=2 bus={tf.bus_secundario} kv={tf.kv_secundario} kVA={tf.kva}"
                )

            elif nome in self.linhas:
                linha = self.linhas[nome]
                dss.append(
                    f"New line.{linha.nome} phases={linha.fases} "
                    f"bus1={linha.bus1} bus2={linha.bus2} "
                    f"r1={linha.r1} x1={linha.x1} length={linha.comprimento} units={linha.unidade}"
                )

            elif nome in self.cargas:
                carga = self.cargas[nome]
                dss.append(
                    f"New load.{carga.nome} phases={carga.fases} model={carga.modelo} "
                    f"bus={carga.bus} kv={carga.kv} kw={carga.kw} kvar={carga.kvar}"
                )

        # Base de tensão e solução
        bases_str = ", ".join(str(b.tensao_kv) for b in self.bases_tensao)
        dss.append(f"Set voltagebases=({bases_str})")
        dss.append("Calcvoltagebases")
        dss.append("Solve")
        dss.append("Show voltages LN Nodes")

        return "\n".join(dss)

    def salvar_em_arquivo(self, caminho):
        with open(caminho, 'w') as f:
            f.write(self.gerar_codigo())
