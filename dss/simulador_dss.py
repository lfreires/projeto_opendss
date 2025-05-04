import os
from py_dss_interface import DSS

class SimuladorDSS:
    def __init__(self, caminho_arquivo_dss):
        self.dss = DSS()
        self.caminho = os.path.abspath(caminho_arquivo_dss)

    def executar(self):
        self.dss.text("Clear")
        self.dss.text(f"Compile \"{self.caminho}\"") 
        self.dss.text("Solve")
        
    def obter_tensoes_por_barra(self):
        barras = self.dss.circuit.buses_names
        print("Barras disponíveis:", self.dss.circuit.buses_names)
        resultado = {}

        for barra in barras:
            self.dss.circuit.set_active_bus(barra)
            tensoes = self.dss.bus.pu_voltages  # lista com [Vre1, Vim1, Vre2, Vim2, ...]
            tensoes_pu = [
                round((tensoes[i]**2 + tensoes[i+1]**2)**0.5, 4)
                for i in range(0, len(tensoes), 2)
            ]
            resultado[barra] = tensoes_pu

        return resultado
