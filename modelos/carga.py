class Carga:
    def __init__(self, nome, fases, modelo, bus, kv, kw, kvar):
        self.nome = nome
        self.fases = fases
        self.modelo = modelo
        self.bus = bus
        self.kv = kv
        self.kw = kw
        self.kvar = kvar

    def gerar_linha_dss(self):
        return (
            f"New Load.{self.nome} phases={self.fases} model={self.modelo} "
            f"bus={self.bus} kv={self.kv} kw={self.kw} kvar={self.kvar}"
        )