# README

Este é o README para a aplicação Streamlit desenvolvida em Python para visualização de dados a partir do Azure Blob Storage. A aplicação carrega dados de dois arquivos CSV, "Em_espera.csv" e "Encerrados.csv", hospedados no Azure Blob Storage, e os exibe utilizando a biblioteca Streamlit.

## Pré-requisitos

- Python
- pip
- Anaconda Navigator (opcional, mas recomendado)

## Configuração do Ambiente Local

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/williamsartijose2023/JusticaStreamlit
   cd seuprojeto

2. **Instale as Dependências:**
   ```bash
   pip install streamlit pandas azure-storage-blob

3. **Execute a Aplicação:**
   ```bash
   streamlit run app.py
  - Abra http://localhost:8501 no seu navegador.

4. **Ambiente Virtual (Anaconda)- Abra um Terminal no Anaconda Navigator:**
    ```bash
   conda activate seuambiente

 5. **Instale as Dependências no Ambiente Virtual:**
    ```bash
     pip install streamlit pandas azure-storage-blob

6. **Execute a Aplicação- No diretório onde se encontra o arquivo app.py, execute::**
    ```bash
     streamlit run app.py
 # Deploy
## Para implantar a aplicação, foi feito o deploy utilizando o Streamlit Sharing.

O aplicativo está disponível em: https://justicaapp-cjtf2pz5qugy4wtikfxqya.streamlit.app/.



