import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient
from io import StringIO

# Adicione o estilo Bootstrap diretamente no HTML
st.markdown(
    """
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    """, unsafe_allow_html=True
)

# Read the content of "styles.css" and apply it
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Crie um card Bootstrap diretamente no Streamlit usando HTML
st.markdown(
    """
     <div class="container mt-5">
    <p class="titulo-css">Tempos de espera</p>
    <p class="subtitulo-css">Saiba quais os locais com o atendimento mais rápido para o <span class="dsc-bold-text">Cartão de Cidadão</span></p>
    
    <div class="container mt-5">
        <div class="row row-cols-1 row-cols-md-4 row-cols-lg-4 g-3">
            <div class="col">
                <div class="card custom-card">
                    <div class="card-body">
                        <p class="card-title">Coimbra</p>
                        <p class="card-text">Conservatória Do Registo Civil, Predial e Comercial</p>
                        <div class="alert alert-light" role="alert">
                            A simple light alert—check it out!
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card custom-card">
                    <div class="card-body">
                        <p class="card-title">Coimbra</p>
                        <p class="card-text">Conservatória Do Registo Civil, Predial e Comercial</p>
                        <div class="alert alert-light" role="alert">
                            A simple light alert—check it out!
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card custom-card">
                    <div class="card-body">
                        <p class="card-title">Coimbra</p>
                        <p class="card-text">Conservatória Do Registo Civil, Predial e Comercial</p>
                        <div class="alert alert-light" role="alert">
                            A simple light alert—check it out!
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card custom-card">
                    <div class="card-body">
                        <p class="card-title">Coimbra</p>
                        <p class="card-text">Conservatória Do Registo Civil, Predial e Comercial</p>
                        <div class="alert alert-light" role="alert">
                            A simple light alert—check it out!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Função para carregar dados do Azure Blob Storage usando SAS token
def load_data_from_azure_with_sas(blob_url, container_name, blob_name, sas_token):
    # Montar a URL completa com o token de SAS
    full_blob_url = f"{blob_url}/{container_name}/{blob_name}?{sas_token}"
    
    # Conectar ao blob
    blob_service_client = BlobServiceClient(account_url=blob_url)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Baixar e ler dados
    blob_data = blob_client.download_blob().readall()
    df = pd.read_csv(StringIO(blob_data.decode('utf-8')))
    
    return df

# Variáveis de conexão
blob_url = "https://prdstoragejusticagovpt.blob.core.windows.net"
container_name = "senhas-irn"
sas_token = "sp=racwdl&st=2023-10-19T16:32:25Z&se=2024-10-20T00:32:25Z&spr=https&sv=2022-11-02&sr=c&sig=Hc8JmVBNn1IXOulo7tWfCX5VP6j0zbqV6%2BwFaaoFqyA%3D"

# Carregar dados com URL completa, container e token de SAS
df_em_espera = load_data_from_azure_with_sas(blob_url, container_name, "Em_espera.csv", sas_token)
df_encerrados = load_data_from_azure_with_sas(blob_url, container_name, "Encerrados.csv", sas_token)

# Exibir os dados no Streamlit
st.header("Dados de Em Espera:")
st.dataframe(df_em_espera)

st.header("Dados de Encerrados:")
st.dataframe(df_encerrados)
