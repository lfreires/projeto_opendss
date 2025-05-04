import pandas as pd
from modelos.transformador import Transformador
from modelos.linha import Linha 
from modelos.carga import Carga 
from modelos.base_tensao import BaseTensao 

class LeitorExcel:
    def __init__(self, caminho_arquivo):
        self.caminho = caminho_arquivo

    def ler_transformadores(self):
        df = pd.read_excel(self.caminho, sheet_name="Transformadores")
        transformadores = []

        for _, linha in df.iterrows():
            tf = Transformador(
                nome=linha["Nome"],
                windings=linha["Windings"],
                bus_primario=linha["Bus Primário"],
                kv_primario=linha["kV Primário"],
                kva=linha["kVA"],
                bus_secundario=linha["Bus Secundário"],
                kv_secundario=linha["kV Secundário"],
                loadloss=linha["%LoadLoss"],
                noloadloss=linha["%NoLoadLoss"],
                xhl=linha["XHL"]
            )
            transformadores.append(tf)

        return transformadores
    
    def ler_linhas(self):
        df = pd.read_excel(self.caminho, sheet_name="Linhas")
        linhas = []

        for _, linha in df.iterrows():
            l = Linha(
                nome=linha["Nome"],
                fases=linha["Fases"],
                bus1=linha["Bus 1"],
                bus2=linha["Bus 2"],
                r1=linha["R1"],
                x1=linha["X1"],
                comprimento=linha["Comprimento"],
                unidade=linha["Unidade"]
            )
            linhas.append(l)

        return linhas
    
    def ler_cargas(self):
        df = pd.read_excel(self.caminho, sheet_name="Cargas")
        cargas = []

        for _, linha in df.iterrows():
            carga = Carga(
                nome=linha["Nome"],
                fases=linha["Fases"],
                modelo=linha["Modelo"],
                bus=linha["Bus"],
                kv=linha["kV"],
                kw=linha["kW"],
                kvar=linha["kvar"]
            )
            cargas.append(carga)

        return cargas
    
    def ler_bases_tensao(self):
        df = pd.read_excel(self.caminho, sheet_name="BaseTensao")
        bases = [BaseTensao(row["Tensão_base (kV)"]) for _, row in df.iterrows()]
        return bases