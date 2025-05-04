class Linha:
    def __init__(self, nome, fases, bus1, bus2, r1, x1, comprimento, unidade):
        self.nome = nome
        self.fases = fases
        self.bus1 = bus1
        self.bus2 = bus2
        self.r1 = r1
        self.x1 = x1
        self.comprimento = comprimento
        self.unidade = unidade

    def gerar_linha_dss(self):
        return (
            f"New Line.{self.nome} phases={self.fases} bus1={self.bus1} bus2={self.bus2} "
            f"r1={self.r1} x1={self.x1} length={self.comprimento} units={self.unidade}"
        )
