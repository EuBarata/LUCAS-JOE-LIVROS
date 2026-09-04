import sqlite3 as sq
import pandas as pd

def conectar():
    conn = sq.Connection("livros.db")
    return conn

def criar_livro(nome_banco ="livros.db"):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS livros (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER NOT NULL,
        status TEXT NOT NULL
        
                )
    
    """)

    conn.commit(nome_banco)
    conn.close(nome_banco)

def cadastrar_livro(titulo,autor,ano_publicacao):

    if ano_publicacao < 2026:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(" INSERT INTO livros VALUES (?,?,?,'status')", (titulo,autor,ano_publicacao))

        conn.commit()
        conn.close()    
        
    return "O livro é de 2026 e não pode ser cadastrado!!"   

def listar_livros(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros where id = ?", (id,))

    resultado = cursor.fetchall()

    columns = ["id","titulo","autor","ano da publicação","status"]

    df = pd.DataFrame(resultado,columns)
    return df
    
def atualizar_livro(status,id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(" UPDATE livros SET status = ? where id = ? ",(status,id))

    conn.commit()
    conn.close()



def deletar_livros(id,status_livro):
    if status_livro == "Lido" or status_livro == "Não Lido":

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(" DELETE FROM livros where id = ?",(id))

        return cursor.rowcount

        
    return "O livro só pode ser deletado se seu status for lido/não lido"
    
        
    
    
    