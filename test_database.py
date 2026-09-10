import unittest # ferramentas para teste
import sqlite3
import os # permite manipular funções  do sistema operacional
import database as db

# Casos de teste 

# classe test_cadastro_livros  
# quando executa a classe, junto dela recebe um objeto unitttest dw teste case 
# que agrupa os métodos ( casos de teste )

class TestCadastrolivros(unittest.TestCase):

# Você é obrigado a criar setUp setDonw eles criam/excluem a caixa de areia

    def setUp(self):

        self.banco_teste = "banco_teste.db"
        db.criar_livro(nome_banco = self.banco_teste)


    def tearDown(self):
        if os.path.exists(self.banco_teste):
                os.remove(self.banco_teste)

# alguma coisa dentro do todo recebe todo  
# ao passar o metodo pra ee mesmo manda ele modificar o espaço cotido nle
    


    def teste_cadastrar_livro_com_sucesso(self):
        
        db.cadastrar_livro("Super","Chester",2005,self.banco_teste)

        conn = sqlite3.connect(self.banco_teste)
        cursor = conn.cursor()

        cursor.execute(" SELECT * FROM livros WHERE titulo = 'Super'")
        livro_salvo = cursor.fetchone ()
        conn.close()

        self.assertIsNotNone(livro_salvo,"O livro deveria ter sido cadastrado")
        self.assertEqual(livro_salvo[1],"Super")
        self.assertEqual(livro_salvo[2],"Chester")
        self.assertEqual(livro_salvo[3],2005)
        self.assertEqual(livro_salvo[4],"Lendo")
    
    
       
    def teste_ano_livro_maior_que_2025(self):

        db.cadastrar_livro("Supernatural","Chester",2026,self.banco_teste)

        conn = sqlite3.connect(self.banco_teste)
        cursor = conn.cursor()

        cursor.execute("SELECT ano_publicacao FROM livros WHERE titulo = 'Supernatural'")

        ano_livro = cursor.fetchone()
        
        conn.close()

        self.assertIsNone(ano_livro, "o livro so deve ser cadastrado se for publicado antes de 2026") 
 
    def teste_deletar_livro_com_sucesso(self):

        conn = sqlite3.connect(self.banco_teste)
        cursor = conn.cursor()

        cursor.execute(" SELECT * FROM livros WHERE titulo = 'Super'")

        self.assertIsNone(cursor.fetchone(), "Livro não encontrado")

        if cursor.fetchone():
            id_livro = cursor.fetchall()[0]
            status = cursor.fetchall()[4]

            msg = db.deletar_livros(id_livro, status, nome_banco= self.banco_teste)
            self.assertTrue(msg)

        conn.close()
        

   
if __name__ == "__main__":
     unittest.main()














