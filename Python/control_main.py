import tkinter as tk
from tkinter import Tk


def login():
    login = Tk()
    login.title("Tela de login")
    login.geometry("270x180")

    frmCaixa = tk.Frame(login)
    frmCaixa.grid(row=0, column=0, pady=25)
    lblUser = tk.Label(frmCaixa, text="User")
    lblUser.grid(row=0, column=0, pady=5)
    entUser = tk.Entry(frmCaixa)
    entUser.grid(row=0, column=1)
    lblPass = tk.Label(frmCaixa, text="Senha")
    lblPass.grid(row=1, column=0, pady=5)
    entPass = tk.Entry(frmCaixa, show="*")
    entPass.grid(row=1, column=1)

    frmButton = tk.Frame(login)
    frmButton.grid(row=1, column=0, padx=75, pady=5)
    btnOk = tk.Button(frmButton, text="Entrar", command=adm)
    btnOk.grid(row=0, column=0)
    btnSair = tk.Button(frmButton, text="Sair", command=login.destroy)
    btnSair.grid(row=0, column=1)

    login.mainloop()


def adm():
    adm = Tk()
    adm.title("Administrator")
    adm.geometry("525x230")

    menubar = tk.Menu(adm)
    # shutdown
    menubar.add_command(label="Desligar Sistema", command=adm.destroy)
    menubar.add_command(label="Sair", command=adm.destroy)
    adm.config(menu=menubar)

    btnControl = tk.Button(adm, text="Painel de Controle")
    btnControl.grid(row=0, column=0, padx=5, pady=5)
    btnRegistro = tk.Button(adm, text="Editor de Registro")
    btnRegistro.grid(row=0, column=1, padx=5, pady=5)
    # control userpasswords2
    btnUser = tk.Button(adm, text="Novo Usuário")
    btnUser.grid(row=0, column=2, padx=5, pady=5)
    # hdwwiz.cpl
    btnDisp = tk.Button(adm, text="Gerenciador de Dispositivos")
    btnDisp.grid(row=1, column=0, padx=5, pady=5)
    # control netconnections
    btnNetConc = tk.Button(adm, text="Conexões de Rede")
    btnNetConc.grid(row=1, column=1, padx=5, pady=5)
    # diskmgmt.msc
    btnDiscos = tk.Button(adm, text="Gerenciador de Discos")
    btnDiscos.grid(row=1, column=2, padx=5, pady=5)
    # compmgmt.msc

    home.destroy()
    adm.mainloop()


home = Tk()
home.geometry("450x230")

menubar = tk.Menu(home)
menubar.add_command(label="Login", command=login)
menubar.add_command(label="Sair", command=home.destroy)

home.config(menu=menubar)

btnWinVer = tk.Button(home, text="Versão Windows")
btnWinVer.grid(row=0, column=0, padx=5, pady=5)
btnCalc = tk.Button(home, text="Calculadora")
btnCalc.grid(row=0, column=1, padx=5, pady=5)

home.mainloop()
