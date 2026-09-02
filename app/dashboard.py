import streamlit as st #importando o streamlit como st (so um nome pra abreviar)

def tela_inicio (): # funcao para mostrar tela inicial
    st.header("Bem-vindo à página inicial!")

def tela_classificacao(): # funcao para mostrar tela de classificação
    st.header("📊 Classificação")
    st.write("A tabela da Premier League aparecerá aqui.")

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