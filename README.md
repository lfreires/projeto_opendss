# 🧠 Simulador de Sistemas Elétricos com OpenDSS e Python

Este projeto realiza a leitura de dados elétricos de uma planilha Excel, gera o código `.dss` para o OpenDSS, executa a simulação e plota os resultados — salvando tudo de volta no Excel com gráficos.

## 🚀 Funcionalidades

- Leitura de transformadores, linhas, cargas e bases de tensão a partir de Excel.
- Geração automática do código `.dss`.
- Execução da simulação via OpenDSS.
- Extração de tensões por barramento.
- Geração de gráfico de linha (tensões pu por barra).
- Escrita dos resultados + gráfico no Excel.

## 🗂 Estrutura de Pastas

```
meu_projeto_opendss/
├── base_opendss.xlsx             # Planilha de entrada e saída
├── main.py                       # Arquivo principal
├── config.py
│
├── dss/
│   ├── gerador_dss.py            # Gera código .dss
│   ├── simulador_dss.py          # Roda o OpenDSS
│   ├── topologia.py              # Ordena elementos via grafo
│   └── gera_grafico.py           # Gera gráfico + insere no Excel
│
├── excel/
│   └── leitor_excel.py           # Leitura da planilha
│
├── modelos/
│   ├── transformador.py
│   ├── linha.py
│   ├── carga.py
│   └── base_tensao.py
```

## 📦 Instalação

1. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como usar

1. Edite o arquivo `base_opendss.xlsx` com seus dados.
2. Execute o projeto:

```bash
python main.py
```

3. O arquivo `saida.dss` será gerado e executado. Os resultados e o gráfico serão salvos na planilha Excel, na aba `Resultados`.

## 🛠 Requisitos

- Python 3.8+
- OpenDSS instalado (e no PATH do sistema)
