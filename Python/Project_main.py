from tkinter import Tk
from tkinter import ttk
from datetime import datetime


def home(user):
    home = Tk()
    home.title("Home")
    # Recupera as dimensões do monitor
    monitor_height = home.winfo_screenheight()
    monitor_width = home.winfo_screenwidth()
    # Usa as dimensões do monitor como parâmetros para criar tela
    home.geometry("%dx%d" % (monitor_width, monitor_height))

    dataHora = datetime.now()
    hoje = dataHora.strftime('%d/%m/%Y %H:%M')

    lblUser = ttk.Label(home, text=user, width=60)
    lblUser.grid(row=1, column=1, padx=13)

    lblData = ttk.Label(home, text=hoje, width=18)
    lblData.grid(row=1, column=2)

    btnSair = ttk.Button(home, command=home.destroy, text="Sair")
    btnSair.grid(row=1, column=5, padx=10, sticky="NSEW")

    home.mainloop()


# DEF para validação do usuário
def submit():
    user = entUser.get()
    senha = entPass.get()
    #print("Login é, ", user)
    #print("Senha é, ", senha)
    login.destroy()
    home(user)


# Tela de Login
login = Tk()
login.title("Tela Login")
login.geometry("210x105")

# Frame com caixas de login e senha
frmBox = ttk.Frame(login)
frmBox.grid(row=1, column=0, pady=5)

lblUser = ttk.Label(frmBox, text="User")
lblUser.grid(row=1, column=0, padx=5)
entUser = ttk.Entry(frmBox, width=13)
entUser.grid(row=1, column=1, pady=5)

lblPass = ttk.Label(frmBox, text="Senha")
lblPass.grid(row=2, column=0)
entPass = ttk.Entry(frmBox, show='*', width=13)
entPass.grid(row=2, column=1, pady=5)

# Frame com botões
frmButton = ttk.Frame(login)
frmButton.grid(row=2, column=0, padx=22, pady=5)
btnSubmit = ttk.Button(frmButton, command=submit, text="Enviar")
btnSubmit.grid(row=1, column=0)

btnExit = ttk.Button(frmButton, command=login.destroy, text="Sair")
btnExit.grid(row=1, column=1)

login.mainloop()
