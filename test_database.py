import unittest
import sqlite3
import os
import database as db

class TestCadastrolivros(unittest.TestCase):

    def setUp(self):

        self.banco_teste = "banco_teste.db"
        db.criar_livro(nome_banco=self.banco_teste)


    def tearDown(self):
        if  os.path.exists(self.banco_teste):
                os.remove(self.banco_teste)

    def teste_cadastrar_aluno_com_sucesso(self):
         
         db.cadastrar_livro("Superatural","Chester",2005,"Lido",self.banco_teste)

         conn = sqlite3.connect(self.banco_teste)
         cursor = conn.cursor()

         cursor.execute(" SELECT * FROM livros WHERE nome = 'Supernatural'")
         livro_salvo = cursor.fetchone  ()
         conn.close()

         self.assertIsNotNone(livro_salvo,"O aluno deveria ter sido cadastrado")
         self.assertEqual(livro_salvo[1],"Supernatural")
         self.assertEqual(livro_salvo[2],"Chester")
         self.assertEqual(livro_salvo[3],2005)
         self.assertEqual(livro_salvo[4],"Lido")

if __name__ == "__main__":
     unittest.main()