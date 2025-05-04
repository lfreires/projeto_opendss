class Transformador:
    def __init__(self, nome, windings, bus_primario, kv_primario, kva, bus_secundario, kv_secundario, loadloss, noloadloss, xhl):
        self.nome = nome
        self.windings = windings
        self.bus_primario = bus_primario
        self.kv_primario = kv_primario
        self.kva = kva
        self.bus_secundario = bus_secundario
        self.kv_secundario = kv_secundario
        self.loadloss = loadloss
        self.noloadloss = noloadloss
        self.xhl = xhl

    def gerar_linha_dss(self):
        return (
            f"New Transformer.{self.nome} Windings={self.windings} "
            f"%loadloss={self.loadloss} %noloadloss={self.noloadloss} XHL={self.xhl}\n"
            f"~ wdg=1 bus={self.bus_primario} kv={self.kv_primario} kVA={self.kva}\n"
            f"~ wdg=2 bus={self.bus_secundario} kv={self.kv_secundario} kVA={self.kva}"
        )
