import database as db
import streamlit as st

db.criar_livro()






st.markdown("""

          
    <style>

.App  {
        
                background-image: url(https://www.fatosdesconhecidos.com.br/wp-content/uploads/2018/01/Dean-lendo-800x418.png);
                background-position: center;
                background-size: cover;
                background-repeat: no-repeat;
                padding: 55px;
                text-align: center;
}

.App h1 {

                font-size: 40px;
                margin-bottom: 10px;
                color: #ff0000;
}

.App p {        
                font-size: 15px;
                color: #ffffff;
}
            
    </style>
    
<div class="App">
    <h1> Bem-vindo ao Livro_BOOK </h1>
    <p>  A melhor loja de livros do BRASIL!!! </p>
</div>
                    """, unsafe_allow_html=True)



abas = st.tabs(["Cadastrar","Visualizar","Atualizar","Excluir"])

with abas[0]:

    st.write("Cadastre seu livro:")
    with st.form("Cadastro de Livros"):

        titulo = st.text_input("Insira o nome do livro")
        autor  = st.text_input(" Insira o nome do autor ")
        ano_pulicacao = st.number_input(" Insira o Ano da publicação ",step=1.00)

        btn = st.form_submit_button("Cadastrar")
        
        if btn:
                db.cadastrar_livro(titulo,autor,ano_pulicacao)
                st.success("O livro foi cadastrado com sucesso")

with abas[1]:

    st.write("Vizualizar Livros")

    with st.form("Vizualizar Livros"):
    
            btn = st.form_submit_button("Livros cadastrados")
            
            if btn:
                livros = db.listar_livros(id)

                for livro in livros:
                    st.success(livro)

with abas[2]:

    st.write("Atualizar Livros")

    with st.form("Atualizar um Livro"):

            status = st.radio ("Escolha o Status",["Lido","Não Lido","Lendo"])

            btn = st.form_submit_button("Atualizar")
            
            if btn:
                livros = db.atualizar_livro(status,id)
                st.success("Livro atualizado com sucesso!")

with abas[3]:

    st.write("Deletar Livros")

    with st.form("Deletar um Livro"):


            status_livro = st.radio ("Escolha o Status",["Lido","Não Lido","Lendo"])  

            btn = st.form_submit_button("Deletar")
            
            if btn:
                resultado = db.deletar_livros(id, status)

                if resultado:
                    st.success("Livro deletado com sucesso!")
                else:
                    st.error("Livro não encontrado.")

    



     

        
        


