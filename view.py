import sqlite3



def connect():
    connectar = sqlite3.connect('dados.db')
    return connectar

def insertBook(titulo, autor, editora, ano_publicacao, isbn):
    connectar = connect()
    connectar.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                VALUES(?, ?, ?, ?, ?)",(titulo, autor, editora, ano_publicacao, isbn))
    
    connectar.commit()
    connectar.close()

def insertUsuarios(nome, sobrenome, endereco, email, telefone):
    connectar = connect()
    connectar.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                VALUES(?, ?, ?, ?, ?)",(nome, sobrenome, endereco, email, telefone))

    
    connectar.commit()
    connectar.close()


def exibirLivros():
    connectar = connect()
    dados = connectar.cursor()
    dados = connectar.execute("SELECT * FROM livros ")
    livros = dados.fetchall()
    connectar.close()
    return livros

   # if not livros:
      #  print("Nenhum livro foi encontrado na biblioteca")
       # return
    
    #print("Livros na biblioteca: ")
   # for livro in livros:
   #    print(f"ID:{livro[0]}")
     #   print(f"Titulo:{livro[1]}")
     #   print(f"Autor:{livro[2]}")
     #   print(f"Editora:{livro[3]}")
      #  print(f"Ano de Publicacao:{livro[4]}")
       # print(f"ISBN:{livro[5]}")
      #  print(f"\n")

def exibirUser():
    connectar = connect()
    dados = connectar.cursor()
    dados = connectar.execute("SELECT * FROM usuarios")
    user = dados.fetchall()
    connectar.close()
    return user
   # if not usuarios:
    #    print("Não temos nenhum usuario cadastrado")
     #   return
    
    #print("Dados do usuario:")
    #for user in usuarios:
     #   print(f"ID:{user[0]}")
      #  print(f"Nome:{user[1]}")
       # print(f"Sobrenome:{user[2]}")
        #print(f"endereco:{user[3]}")
     #   p#rint(f"Email:{user[4]}")
    #    pr#int(f"telefone:{user[5]}")
        #print(f"\n")


def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    connectar = connect()
    connectar.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                      VALUES(?, ?, ?, ? )", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    connectar.commit()
    connectar.close()



def getBooksOnLoan():
    connectar = connect()
    result= connectar.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, \
                                emprestimos.data_devolucao FROM livros\
                                INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                                INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                                WHERE emprestimos.data_devolucao IS NULL ").fetchall()
    connectar.close()
    return result



def updateLoanReturnDate(id_emprestimo, data_devolucao):
    connectar = connect()
    connectar.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao,id_emprestimo))
    connectar.commit()
    connectar.close()








#insertBook("dom", "miguel", "gabrielzito", 1605, "123456")
#
#print("-----------------------------------------------------------------------------------------------------------------------------")

#exibirLivros()
#print("-----------------------------------------------------------------------------------------------------------------------------")

#user = insertUsuarios("dom", "miguel", "gabrielzito", "1605", "123456")
exibirUser()
#print("-----------------------------------------------------------------------------------------------------------------------------")

#insert_loan(1,1, "2022-09-24", None)
#print(getBooksOnLoan())

#updateLoanReturnDate(1,"2022-09-24")
