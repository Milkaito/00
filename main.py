import tkinter.messagebox
from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

cor1 = "DeepSkyBlue3"
cor2 = "DeepSkyBlue4"
cor3 = "PaleGreen3"

principal = Tk()
principal.title("Cadastro de usuários")
principal.config(background = cor1)
principal.geometry("800x300")

def cadastrar():
  if  nome.get() == "" or nascimento.get() == ""  or email.get() == "":
    tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!")
    

#variáveis
nome = StringVar()
nascimento = StringVar()
email = StringVar()
senha=StringVar()

# frame
topo = Frame(principal, width=300, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
esquerda = Frame(principal, width=300, height=300, bd=1, relief="raise", background=cor1)
esquerda.pack(side=LEFT)

Forms = Frame(esquerda, width=300, height=300, background=cor1)
Forms.pack(side=TOP)
Buttons = Frame(esquerda, width=100, height=100, background=cor1, relief="raise")
Buttons.pack(side=BOTTOM)

# labels
txt_titulo = Label(topo, width=600, font=('arial', 20), text = "Cadastro", background=cor2)
txt_titulo.pack()
txt_nome = Label(Forms, text="Nome:", font=('arial', 15), bd=15, background=cor1)
txt_nome.grid(row=0, stick="e")
txt_email = Label(Forms, text="E-mail:", font=('arial', 15), bd=15, background=cor1)
txt_email.grid(row=2, stick="e")
txt_nascimento = Label(Forms, text="Nascimento:", font=('arial', 15), bd=15, background=cor1)
txt_nascimento.grid(row=1, stick="e")
txt_senha= Label(Forms, text="Senha:", font=('arial', 15), bd=15, background=cor1)
txt_senha.grid(row=3, stick="e")


# entrys
nome = Entry(Forms, textvariable=nome, width=30)
nome.grid(row=0, column=1)
nascimento = Entry(Forms, textvariable=nascimento, width=25)
nascimento.grid(row=1, column=1)
email = Entry(Forms, textvariable=email, width=30)
email.grid(row=2, column=1)
senha = Entry(Forms, textvariable=email, width=25)
senha.grid(row=3, column=1)

btn_cadastrar = Button(Buttons, width=15, text="Cadastrar", command=cadastrar)
btn_cadastrar.pack(side=LEFT)




principal.mainloop()

