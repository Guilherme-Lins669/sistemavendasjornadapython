# é necessário no terminal eu escrever = cd ".\Sistema de Vendas e Gestão Online - Aula04"

# Para rodar código do streamlit tem que digitar no terminal = streamlit run main.py

# st.title() = ele muda o título da aba do navegador
# st.tabs() = ele cria abas dentro do site, permitindo separar diferentes conteúdos
# st.navigation() = ele cria uma navegação entre diferentes páginas do sistema

# O navigation e o tabs são bons para criar menus ou facilitar a navegação entre diferentes páginas e conteúdos do sistema

# Título - Sistema de Vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produtos - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Vendas
        # Quando eu clicar no botão -> adicionar a venda na tabela

# Seção Vendas Cadastradas
    # Tabela com as Vendas

# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por produto

# Ferramentas a ser usada:
    # streamlit
    # pandas
    # plotly

# Importando o streamlit para podermos começar a fazer o sistema
import streamlit as st
# Importando o pandas para poder trabalhar com base de dados
import pandas as pd
# Importando o plotly.express para podermos fazer os gráficos, os gráficos pré-prontos estão no .express, por isso importamos desse jeito
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

# Titulos e Seções
# Titulo
st.write("# Sistemas de Vendas") # As "#" servem para mudar o tamanho do titulo, titulo maior 1#

# Seção de cadastro de vendas
# st.sidebar: para fazer uma barra lateral, tudo que quisermos colocar numa barra lateral, o "st.sidebar." antes do código

st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data") # input de data para permitir o usuário selecionar uma data
# Se eu colocar um valor min ou um valor max, eu posso cadastrar vendas de datas anteriores ou posteriores para assim limitar a data
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"]) # uma caixa de seleção, para permitir que o usuário selecione o vendedor, junto do nome da caixa
# e a lista do nome dos vendedores
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", step=1) # input de número para o usuário selecionar a quantidade de produtos
# o "step=" faz pular de número em número, nesse caso pular de 1 em 1
valor = st.sidebar.number_input("Valor") # input de número para o usuário selecionar o valor
botao_cadastrar = st.sidebar.button("Cadastrar Venda") # botão para o usuário clicar e cadastrar a venda

# logica de cadastro
if botao_cadastrar:
    
    if valor <= 0 or quantidade <= 0 or vendedor == "": 
        st.warning("Alguma Informação está faltando!") # Irá emitir uma aviso caso o valor esteja zero
    else:  
        nova_venda = [str(data), # Deixando a data como texto nos criamos uma trava de segurança para evitar problemas
                       vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas) # Com isso pegaremos a última linha para adicionar a nova venda
        tabela_vendas.loc[ultima_linha] = nova_venda # Com o .loc podemos localizar uma linha da tabela, usando a ultima_linha faremos ela pegar a ultima linha
        # assim fazendo com que a nova venda fique nela
        tabela_vendas.to_csv("vendas.csv", index=False) # Desse jeito, a tabela será atualizada, sem os indices falsos, assim a cada nova venda, substituirá a tabela antiga, pela nova com a última venda adicionada
        st.success("Venda Cadastrada") # Irá aparecer uma mensagem mostrando que a venda foi cadastrada

# Seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) # o dateframe, é uma "tabela pro pandas", onde vai mostrar nossa tabela de vendas

# Seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum() # Queremos pegar a coluna da nossa base de dados que iremos somar para calcular o faturamento total
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de Barra/Coluna -> Venda por vendedor
# Cria o gráfico
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto") # Gráfico de barras
# No gráfico de barras tem que especificar o eixo "x" e o "y"

# Exibir gráfico
st.plotly_chart(grafico1) # Desse jeito o gráfico sera exibido no site

# Gráfico de Pizza -> Venda por produto
# Cria o gráfico
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.4) # Gráfico de pizza
# No gráfico de pizza nos separamos pelos nomes e valores que serão exibidos
# o hole= coloca um buraco no meio do gráfico de pizza

# Exibir gráfico
st.plotly_chart(grafico2) # Desse jeito o gráfico sera exibido no site