import sqlite3 as sq
import pandas as pd

def conectar(nome_banco = "livros.db"):
    conn = sq.Connection(nome_banco)
    return conn

def criar_livro(nome_banco ="livros.db"):
    conn = conectar(nome_banco)
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS livros (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER NOT NULL,
        status TEXT NOT NULL
        
                )
    
    """)

    conn.commit()
    conn.close()

def cadastrar_livro(titulo,autor,ano_publicacao, nome_banco ="livros.db"):


    if ano_publicacao < 2026:
        return False, "O livro é de 2026 e não pode ser cadastrado!!"
    
    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute(" INSERT INTO livros (titulo,autor,ano_publicacao,status) VALUES (?,?,?, 'Lendo')", (titulo,autor,ano_publicacao))

    conn.commit()
    conn.close()    


    return True, "Livro cadastrado com sucesso!"
        
       

def listar_livros(id, nome_banco = "livros.db"):
    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros where id = ?", (id,))

    resultado = cursor.fetchall()

    columns = ["id","titulo","autor","ano da publicação","status"]

    df = pd.DataFrame(resultado,columns)

    cursor.close()
    return df

def atualizar_livro(status,id, nome_banco = "livros.db"):
    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute(" UPDATE livros SET status = ? where id = ? ",(status,id))

    conn.commit()
    conn.close()



def deletar_livros(id,status_livro, nome_banco = "livros.db"):
    if status_livro == "Lido" or status_livro == "Não Lido":
        return "O livro só pode ser deletado se seu status for lido/não lido"
    
    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute(" DELETE FROM livros where id = ?",(id))

    conn.commit()
    conn.close()

    return cursor.rowcount

   


       
    

        
   



    
    