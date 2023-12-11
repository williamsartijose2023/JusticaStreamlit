import streamlit as st
import pandas as pd
from azure.storage.blob import BlobServiceClient
from io import StringIO

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
