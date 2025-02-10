from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from view import*
from tkinter import messagebox
from datetime import date
from datetime import datetime

hoje = datetime.today()


co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#E9A178"
co7 = "#3fbfb9"
co8 = "#262328"
co9 = "e9edf5"
co10 = "6e8faf" 
co11 = "#f2f4f2"


def criarJanela():
    global janela
    janela = Tk()
    janela.title("")
    janela.geometry('770x330')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    style = Style(janela)
    style.theme_use("clam")



def criarFrameCima():
    global frameCima
    frameCima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
    frameCima.grid(row=0, column=0, columnspan=2, sticky = NSEW)
    return frameCima

def criarFrameEsquerdo():
    global frameEsquerdo
    frameEsquerdo = Frame(janela, width=150, height= 265, bg = co4, relief= "solid")
    frameEsquerdo.grid(row=1, column=0, sticky=NSEW) 
    return frameEsquerdo

def criarFrameDireito():
    global frameDireito
    frameDireito = Frame(janela, width=500, height=265, bg=co1, relief="raised")
    frameDireito.grid(row=1, column=1, sticky=NSEW)


def logo(frame):
    # Definindo um caminho absoluto para a imagem e verificando se ela carrega corretamente
    try:
        app_img = Image.open("C:/Users/Gabriel/Desktop/livros/imagem/logo.png")
        app_img = app_img.resize((40, 40))
        app_img = ImageTk.PhotoImage(app_img)

        # Adicionando o Label ao frame e mantendo a referência da imagem
        appLogo = Label(frame, image=app_img, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
        appLogo.image = app_img  # Salvando a referência da imagem para evitar descarte
        appLogo.place(x=5, y=5)

    except Exception as e:
        print("Erro ao carregar a imagem:", e)

    appTitle = Label(frame, text=" Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW, font='Verdana 15 bold', bg=co6, fg=co1)
    appTitle.place(x=50, y=7)

    appLinha = Label(frame, width=770, height=1, padx=5, anchor=NW, font='Verdana 1',bg=co3, fg=co1)
    appLinha.place(x=0, y=47)



#Novo usuario
def novoUsuario():
    global imgSave

    def adicionar():
        firstName = entryNome.get()
        lastName = entrySobreNome.get()
        andress = entryEndereco.get()
        email = entryEmail.get()
        phoneNumber = entryTelefone.get()

        lista = [firstName, lastName, andress, email, phoneNumber]
        for i in lista:
            if i == '':
                         
                messagebox.showerror('Erro', 'Preencha todos os campos ')
                return
            

        insertUsuarios(firstName, lastName, andress, email, phoneNumber)

        messagebox.showinfo('Usuario inserido com Sucesso')
        #limpando os campos de entradas
        entryNome.delete(0,END)
        entrySobreNome.delete(0,END)
        entryEndereco.delete(0,END)
        entryEmail.delete(0,END)
        entryTelefone.delete(0,END)


    appUser = Label(frameDireito, text="Inserir um novo usuário ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    appUser.grid(row=0, column=0, columnspan=4, sticky=NSEW)


    appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Ivy 1'), bg=co3, fg=co1)
    appLinha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    #Nome
    labelNome = Label(frameDireito, text="Primeiro nome", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelNome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    entryNome = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryNome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    #---------------------------------------------------------------------------------------------------------
    #Sobrenome --------------
    labelSobreNome = Label(frameDireito, text="Sobrenome ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelSobreNome.grid(row=3, column=0, padx=5, pady=5, sticky= NSEW)
    
    entrySobreNome = Entry(frameDireito, width=25, justify='left', relief='solid')
    entrySobreNome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    #---------------------------------------------------------------------------------------------------------
    #Endereço
    labelEndereco = Label(frameDireito, text="Endereço", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelEndereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    entryEndereco = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryEndereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)
   #---------------------------------------------------------------------------------------------------------
    #Email
    labelEmail= Label(frameDireito, text="E-mail", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelEmail.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    entryEmail = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryEmail.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)
       #---------------------------------------------------------------------------------------------------------
    #N° de telefone
    labelTelefone= Label(frameDireito, text="Número de telefone", anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
    labelTelefone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    entryTelefone = Entry(frameDireito,width=25, justify='left', relief='solid')
    entryTelefone.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)
    #---------------------------------------------------------------------------------------------------------
    #Botão Salvar
    imgSave = Image.open('imagem/save.png')
    imgSave = imgSave.resize((18,18))
    imgSave = ImageTk.PhotoImage(imgSave)
    buttonSave = Button(frameDireito,command=adicionar ,image=imgSave, compound=LEFT, width=100,anchor=NW, text='Save', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonSave.grid(row=7, column=1, pady=5, sticky=NSEW)
    buttonSave.image = imgSave


def verUsuarios():
    appUser = Label(frameDireito, text="Exibir todos os usuarios ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    appUser.grid(row=0, column=0, columnspan=4, sticky=NSEW)


    appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Ivy 1'), bg=co3, fg=co1)
    appLinha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = exibirUser()
    if dados is None:
        print("Aviso: Nenhum dado foi retornado por `exibirUser`. `dados` está sendo definido como uma lista vazia.")
        dados = []

   #creating a treeview with dual scrollbars
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree

    tree = ttk.Treeview(frameDireito, selectmode="extended",
                        columns=list_header, show="headings")
   # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)

  #  horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireito, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireito.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)



def novoLivro():
    
    global imgSave

    def adicionar():
        title = entryTitulo.get()
        author = entryAutor.get()
        publisher = entryEditora.get()
        yearOfPublication = entryAno_publicacao.get()
        isbn = entryIsbn.get()

        lista = [title, author, publisher, yearOfPublication, isbn]
        for i in lista:
            if i == '':
                         
                messagebox.showerror('Erro', 'Preencha todos os campos ')
                return


        insertBook(title, author, publisher, yearOfPublication, isbn)

        messagebox.showinfo('Livro inserido com Sucesso')
        #limpando os campos de entradas
        entryTitulo.delete(0,END)
        entryAutor.delete(0,END)
        entryEditora.delete(0,END)
        entryAno_publicacao.delete(0,END)
        entryIsbn.delete(0,END)


    appUser = Label(frameDireito, text="Inserir um novo livro ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    appUser.grid(row=0, column=0, columnspan=4, sticky=NSEW)


    appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Ivy 1'), bg=co3, fg=co1)
    appLinha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
     
    #Titulo --------------
    labelTitulo = Label(frameDireito, text="Titulo", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelTitulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    entryTitulo = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryTitulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    #---------------------------------------------------------------------------------------------------------
    #Autor --------------
    labelAutor = Label(frameDireito, text="Autor ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelAutor.grid(row=3, column=0, padx=5, pady=5, sticky= NSEW)
    
    entryAutor = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryAutor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    #---------------------------------------------------------------------------------------------------------
    #EDitora
    labelEditora = Label(frameDireito, text="Editora", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelEditora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    entryEditora = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryEditora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)
   #---------------------------------------------------------------------------------------------------------
    #Ano da publicação
    labelAno_publicacao= Label(frameDireito, text="Ano da publicação", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelAno_publicacao.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    entryAno_publicacao = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryAno_publicacao.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)
       #---------------------------------------------------------------------------------------------------------
    #ISBN
    labelIsbn= Label(frameDireito, text="ISBN", anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
    labelIsbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    entryIsbn = Entry(frameDireito,width=25, justify='left', relief='solid')
    entryIsbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    #Botão Salvar
    imgSave = Image.open('imagem/save.png')
    imgSave = imgSave.resize((18,18))
    imgSave = ImageTk.PhotoImage(imgSave)
    buttonSave = Button(frameDireito,command=adicionar ,image=imgSave, compound=LEFT, width=100,anchor=NW, text='Save', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonSave.grid(row=7, column=1, pady=5, sticky=NSEW)
    buttonSave.image = imgSave



def verLivro():
     appUser = Label(frameDireito, text="Exibir todos os livros ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
     appUser.grid(row=0, column=0, columnspan=4, sticky=NSEW)


     appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Ivy 1'), bg=co3, fg=co1)
     appLinha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

     dados = exibirLivros()
     if dados is None:
        print("Aviso: Nenhum dado foi retornado por `exibirLivro`. `dados` está sendo definido como uma lista vazia.")
        dados = []

   #creating a treeview with dual scrollbars
     list_header = ['ID','Titulo','Autor','Editora','Ano de publicação','ISBN']
    
     global tree

     tree = ttk.Treeview(frameDireito, selectmode="extended",
                        columns=list_header, show="headings")
   # vertical scrollbar
     vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)

  #  horizontal scrollbar
     hsb = ttk.Scrollbar(frameDireito, orient="horizontal", command=tree.xview)
 
     tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

     tree.grid(column=0, row=2, sticky='nsew')
     vsb.grid(column=1, row=2, sticky='ns')
     hsb.grid(column=0, row=3, sticky='ew')
     frameDireito.grid_rowconfigure(0, weight=12)

     hd=["nw","nw","nw","nw","nw","nw"]
     h=[20,80,80,120,120,76,100]
     n=0

     for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

     for item in dados:
        tree.insert('', 'end', values=item)


def realizarEmprestimo():
    global imgSave
    
    def adicionar():
        idLivro = entryIdLivro.get()
        idUser = entryIdUser.get()
       
    
        lista = [idLivro, idUser]

        for i in lista:
            if i== '':
                messagebox.showerror('Erro', 'Prencha todos os campos')

        insert_loan(idLivro, idUser, hoje, None)   

        messagebox.showinfo('Sucesso', 'Emprestimo realizado com sucesso')     
        entryIdLivro.delete(0,END)
        entryIdUser.delete(0,END)


    appUser = Label(frameDireito, text="Realizar emprestimo ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    appUser.grid(row=0, column=0, columnspan=3, sticky=NSEW)


    appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    appLinha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    #IDLivro
    labelIdLivro = Label(frameDireito, text="Digite Id do Livro", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelIdLivro.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    entryIdLivro = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryIdLivro.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #IdUser
    labelIdUser = Label(frameDireito, text="Digite Id do Usuario", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelIdUser.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    entryIdUser = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryIdUser.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #Botão Salvar
    imgSave = Image.open('imagem/save.png')
    imgSave = imgSave.resize((18,18))
    imgSave = ImageTk.PhotoImage(imgSave)
    buttonSave = Button(frameDireito,command=adicionar ,image=imgSave, compound=LEFT, width=100,anchor=NW, text='Save', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonSave.grid(row=7, column=1, pady=5, sticky=NSEW)
    buttonSave.image = imgSave



def verLivrosEmprestados():

    appUser = Label(frameDireito, text="Todos os livros emprestados  ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    appUser.grid(row=0, column=0, columnspan=4, sticky=NSEW)


    appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Ivy 1'), bg=co3, fg=co1)
    appLinha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = []
    bookOnLoan = getBooksOnLoan()

    for book in bookOnLoan:
        dado = [f"{book[0]}", f"{book[1]} {book[2]}", f"{book[3]}", f"{book[4]}" ]
        dados.append(dado)
    

   #creating a treeview with dual scrollbars
    list_header = ['Titulo','Nome do usuário','D. emprestimo','D. devolução']
    
    global tree

    tree = ttk.Treeview(frameDireito, selectmode="extended",
                        columns=list_header, show="headings")
   # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)

  #  horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireito, orient="horizontal", command=tree.xview)
 
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireito.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","ne","ne","ne","ne"]
    h=[120,170,90,90,100,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


def devolucaoEmprestimo():
    global imgSave
    
    def adicionar():
        idLoan = entryIdEmprestimo.get()
        ReturnData = entryDataDeRetorno.get()
       
    
        lista = [idLoan, ReturnData]

        for i in lista:
            if i== '':
                messagebox.showerror('Erro', 'Prencha todos os campos')

        updateLoanReturnDate(idLoan, ReturnData)   

        messagebox.showinfo('Sucesso', 'Emprestimo realizado com sucesso')     
        entryIdEmprestimo.delete(0,END)
        entryDataDeRetorno.delete(0,END)


    appUser = Label(frameDireito, text="Atualizar a data de devolução ", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    appUser.grid(row=0, column=0, columnspan=3, sticky=NSEW)


    appLinha = Label(frameDireito, width=400, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    appLinha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    #IDLivro
    labelIdDataDeRetorno = Label(frameDireito, text="Nova data de Devolucao ( formato: AAAA-MM-DD)", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelIdDataDeRetorno.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    entryDataDeRetorno = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryDataDeRetorno.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #IdUser
    labelIdEmprestimo = Label(frameDireito, text="Digite Id do Emprestimo", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    labelIdEmprestimo.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    entryIdEmprestimo = Entry(frameDireito, width=25, justify='left', relief='solid')
    entryIdEmprestimo.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #Botão Salvar
    imgSave = Image.open('imagem/save.png')
    imgSave = imgSave.resize((18,18))
    imgSave = ImageTk.PhotoImage(imgSave)
    buttonSave = Button(frameDireito,command=adicionar ,image=imgSave, compound=LEFT, width=100,anchor=NW, text='Save', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonSave.grid(row=7, column=1, pady=5, sticky=NSEW)
    buttonSave.image = imgSave


#Função para controlar o menu

def control(i):

    #novo usuario
    if i == 'Novo Usuario' :
        for widget in frameDireito.winfo_children():
            widget.destroy


        #Chamando a função novo usuario  
        novoUsuario()  

    if i =='Exibir todos os usuarios':
        for widget in frameDireito.winfo_children():
            widget.destroy


        verUsuarios()

    if i== "Novo Livro":
        for widget in frameDireito.winfo_children():
            widget.destroy

     
        novoLivro()      

    if i == 'Exibir todos os livros':
        for widget in frameDireito.winfo_children():   
            widget.destroy
        
        verLivro()    


    if i == 'Realizar emprestimo':
        for widget in frameDireito.winfo_children():
            widget.destroy    


        realizarEmprestimo()

    if i == 'Livros emprestados':
        for widget in frameDireito.winfo_children():
            widget.destroy

        verLivrosEmprestados()    

    if i == 'Devolucao de Emprestimo':
        for widget in frameDireito.winfo_children():
            widget.destroy

        devolucaoEmprestimo()      


def menu():
    imgUser = Image.open('imagem/add.png')
    imgUser = imgUser.resize((18,18))
    imgUser = ImageTk.PhotoImage(imgUser)
    buttonUser = Button(frameEsquerdo,command=lambda: control('Novo Usuario') ,image=imgUser, compound=LEFT, anchor=NW, text=' Novo Usuario', bg=co4, fg=co1,font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonUser.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)
    buttonUser.image = imgUser


    imgNewBook = Image.open('imagem/add.png')
    imgNewBook = imgNewBook.resize((18,18))
    imgNewBook = ImageTk.PhotoImage(imgNewBook)
    buttonNewBook = Button(frameEsquerdo,command=lambda: control('Novo Livro') ,image=imgNewBook, compound=LEFT, anchor=NW, text=' Novo Livro',bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief= GROOVE)
    buttonNewBook.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)
    buttonNewBook.image=imgNewBook


    imgAllBooks = Image.open('imagem/livro.png')
    imgAllBooks = imgAllBooks.resize((18,18))
    imgAllBooks = ImageTk.PhotoImage(imgAllBooks)
    buttonAllBooks = Button(frameEsquerdo,command=lambda: control('Exibir todos os livros') ,image= imgAllBooks, compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE,relief=GROOVE )
    buttonAllBooks.grid( row=2,column=0, sticky=NSEW, padx=5, pady=6)
    buttonAllBooks.image = imgAllBooks

    imgAllUser = Image.open('imagem/user.png')
    imgAllUser = imgAllUser.resize((18,18))
    imgAllUser = ImageTk.PhotoImage(imgAllUser)
    buttonAllUser = Button(frameEsquerdo,command=lambda: control('Exibir todos os usuarios') ,image=imgAllUser, compound=LEFT, anchor=NW, text=' Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'),overrelief=RIDGE, relief=GROOVE)
    buttonAllUser.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)
    buttonAllUser.image = imgAllUser

    #Novo Emprestimo
    imgNewLoan = Image.open('imagem/add.png')
    imgNewLoan = imgNewLoan.resize((18,18))
    imgNewLoan = ImageTk.PhotoImage(imgNewLoan)
    buttonNewLoan = Button(frameEsquerdo,command=lambda: control('Realizar emprestimo') ,image=imgNewLoan, compound=LEFT, anchor=NW, text=' Realizar  emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonNewLoan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)
    buttonNewLoan.image = imgNewLoan


    imgLoanReturn = Image.open('imagem/update.png')
    imgLoanReturn = imgLoanReturn.resize((18,18))
    imgLoanReturn = ImageTk.PhotoImage(imgLoanReturn)
    buttonLoanReturn = Button(frameEsquerdo,command=lambda: control('Devolucao de Emprestimo') ,image=imgLoanReturn, compound=LEFT, anchor=NW, text=' Devolução de um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonLoanReturn.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)
    buttonLoanReturn.image = imgLoanReturn

    #Livros Emprestados
    imgBorrowedBooks = Image.open('imagem/carrinho.png')
    imgBorrowedBooks = imgBorrowedBooks.resize((18,18))
    imgBorrowedBooks = ImageTk.PhotoImage(imgBorrowedBooks)
    buttonBorrowedBooks = Button(frameEsquerdo,command=lambda: control('Livros emprestados') ,image=imgBorrowedBooks, compound=LEFT, anchor=NW, text=' Livros emprestados', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    buttonBorrowedBooks.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)
    buttonBorrowedBooks.image = imgBorrowedBooks






criarJanela()
framecima = criarFrameCima()  
criarFrameEsquerdo()
criarFrameDireito()
logo(frameCima)
menu()
janela.mainloop()
