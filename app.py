import database as db
import streamlit as st

db.criar_livro()
db.listar_livros
db.cadastrar_livro()
db.atualizar_livro()
db.deletar_livros()


st.markdown("""

          
    <style>

.app img {
        
                background-image: url("https://tse4.mm.bing.net/th/id/OIP.AlcQ8fUa0m-7kTzihpy3IQHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3");
                background-position: center;
                background-size: cover;
                background-repeat: no-repeat;
}

.app h1 {

                font-size: 40px;
                margim-bottom: 10px;
                color: #ff0000;
}

.app p {        
                font-size: 10px;
                color: #888888;
                

}
            
    </style>
    
            <div class="App">
                <h1> "Bem-vindo ao Livro_BOOK" </h1>
                <p>  "A melhor loja de livros do BRASIL!!!" </P>
            </div>
                    """, unsafe_allow_html=True)



abas = st.tabs(["Cadastrar","Visualizar","Atualizar","Excluir"])

with abas[0]:

    st.write("Cadastre seu livro:")
    with st.form("Cadastro de Livros"):

        titulo = st.text_input("Insira o nome do livro")
        autor  = st.text_input(" Insira o nome do autor ")
        ano_pulicacao = st.number_input(" Inisra o Ano da publicação ")

        btn = st.form_submit_button("Cadastrar")
        
        if btn:
               st.success("O livro foi cadastrado com sucesso")

with abas[1]:
     

        
        


