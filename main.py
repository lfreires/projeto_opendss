import os
from excel.leitor_excel import LeitorExcel
from dss.gerador_dss import GeradorDSS
from dss.simulador_dss import SimuladorDSS
from dss.topologia import montar_conexoes, ordenar_por_topologia
from dss.gera_grafico import gerar_grafico, inserir_grafico_no_excel

# Caminho do Excel
caminho_excel = os.path.join(os.path.dirname(__file__), "base_opendss.xlsx")
leitor = LeitorExcel(caminho_excel)

# Leitura dos dados
transformadores = leitor.ler_transformadores()
linhas = leitor.ler_linhas()
cargas = leitor.ler_cargas()
bases = leitor.ler_bases_tensao()

# Monta grafo e ordena os elementos por topologia
conexoes = montar_conexoes(transformadores, linhas, cargas)
ordem = ordenar_por_topologia(conexoes)

# Gera o .dss
gerador = GeradorDSS(transformadores, linhas, cargas, bases, ordem)
codigo = gerador.gerar_codigo()

# Visualiza o código
print("---- CÓDIGO DSS GERADO ----")
print(codigo)

# Salva o .dss
caminho_saida_dss = os.path.abspath("saida.dss")
gerador.salvar_em_arquivo(caminho_saida_dss)

# Executa a simulação
simulador = SimuladorDSS(caminho_saida_dss)
simulador.executar() 

resultados = simulador.obter_tensoes_por_barra()

for barra, tensoes in resultados.items():
    print(f"{barra}: {tensoes}")

# Gera gráfico e insere no Excel
gerar_grafico(resultados)
inserir_grafico_no_excel(caminho_excel, resultados)