import sqlite3

# Estabelecendo a conexão com o banco de dados
connectar = sqlite3.connect('dados.db')

# Criando a tabela de livros
connectar.execute('''CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT,
                    autor TEXT,
                    editora TEXT,
                    ano_publicacao INTEGER,
                    isbn TEXT)''')

# Criando a tabela de usuários
connectar.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    sobrenome TEXT,
                    endereco TEXT,
                    email TEXT,
                    telefone TEXT)''')

# Criando a tabela de empréstimos
connectar.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                    id INTEGER PRIMARY KEY,
                    id_livro INTEGER,
                    id_usuario INTEGER,
                    data_emprestimo TEXT,
                    data_devolucao TEXT,
                    FOREIGN KEY(id_livro) REFERENCES livros(id),
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id))''')

# Salvando as alterações e fechando a conexão
connectar.commit()
connectar.close()
