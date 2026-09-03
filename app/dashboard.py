import streamlit as st #importando o streamlit como st (so um nome pra abreviar)
from src.coleta.premier_league import coletar_classificacao

def tela_inicio (): # funcao para mostrar tela inicial
    st.header("Bem-vindo à página inicial!")

def tela_classificacao(): # funcao para mostrar tela de classificação
    st.header("📊 Classificação")
    st.write("A tabela da Premier League aparecerá aqui.")

    tabela = coletar_classificacao() #recebe a tabela da funcao do arquivo premier_league.py
    st.dataframe(tabela, hide_index=True) #mostra a tabela escondendo a coluna de indice

st.set_page_config( #informações da aba
    page_title="Dashboard Premier League",
    page_icon="⚽",
)

st.title("⚽ Dashboard Premier League") #titulo principal <h1>

st.sidebar.title("Menu") #<criando uma barra letareal com titulo "Menu">

pagina = st.sidebar.radio( # menu de navegação entre as telas
    "Navegação",
    ["Início", "Classificação"]
)

# mostrando tela escolhida
if(pagina == "Início") :
    tela_inicio()
elif(pagina == "Classificação"):
    tela_classificacao()