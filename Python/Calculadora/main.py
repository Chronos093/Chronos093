from tkinter import Tk
import tkinter

x = []

def tela(n):
  x.append(n)
  lbl_tela = tkinter.Label(grd_tela01, text=n, height = 3, width = 15)
  lbl_tela.grid(column=0, row=0)

def soma():
  qtd_lista = len(x)
  i = 0
  s = 0
  while i < qtd_lista:
    s = x[i] + s
    i = i + 1
  lbl_tela = tkinter.Label(grd_tela01, text=s, height = 3, width = 15)
  lbl_tela.grid(column=0, row=0)

  x.clear()

def sub():
  qtd_lista = len(x) - 1
  i = qtd_lista
  s = 0
  while i >= 0:
    s = x[i] - s
    i = i - 1
  lbl_tela = tkinter.Label(grd_tela01, text=s, height = 3, width = 15)
  lbl_tela.grid(column=0, row=0)

  x.clear()
  
if __name__ == "__main__": 
  root = Tk()
  root.geometry('190x230+25+25')
  root.title("Calculadora")

  grd_tela01 = tkinter.Frame(root)
  grd_tela01.grid(column=0, row=0)
  grd_tela02 = tkinter.Frame(root)
  grd_tela02.grid(column=0, row=1)
  grd_tela03 = tkinter.Frame(root)
  grd_tela03.grid(column=0, row=2)
  grd_tela04 = tkinter.Frame(root)
  grd_tela04.place(x=135, y=48)

  lbl_tela = tkinter.Label(grd_tela01, height = 3, width = 5)
  lbl_tela.grid(column=0, row=0)

  btn_9 = tkinter.Button(grd_tela02, text=9, height = 2, width = 2, command=lambda: tela(9))
  btn_9.grid(column=2, row=1)
  btn_8 = tkinter.Button(grd_tela02, text=8, height = 2, width = 2, command=lambda: tela(8))
  btn_8.grid(column=1, row=1)
  btn_7 = tkinter.Button(grd_tela02, text=7, height = 2, width = 2, command=lambda: tela(7))
  btn_7.grid(column=0, row=1)
  btn_6 = tkinter.Button(grd_tela02, text=6, height = 2, width = 2, command=lambda: tela(6))
  btn_6.grid(column=2, row=2)
  btn_5 = tkinter.Button(grd_tela02, text=5, height = 2, width = 2, command=lambda: tela(5))
  btn_5.grid(column=1, row=2)
  btn_4 = tkinter.Button(grd_tela02, text=4, height = 2, width = 2, command=lambda: tela(4))
  btn_4.grid(column=0, row=2)
  btn_3 = tkinter.Button(grd_tela02, text=3, height = 2, width = 2, command=lambda: tela(3))
  btn_3.grid(column=2, row=3)
  btn_2 = tkinter.Button(grd_tela02, text=2, height = 2, width = 2, command=lambda: tela(2))
  btn_2.grid(column=1, row=3)
  btn_1 = tkinter.Button(grd_tela02, text=1, height = 2, width = 2, command=lambda: tela(1))
  btn_1.grid(column=0, row=3)
  btn_0 = tkinter.Button(grd_tela03, text=0, height = 2, width = 8, command=lambda: tela(0))
  btn_0.grid(column=2, row=4)
  btn_dot = tkinter.Button(grd_tela03, text=".", height = 2, width = 2)
  btn_dot.grid(column=1, row=4)

  btn_soma = tkinter.Button(grd_tela04, text="+", height = 3, width = 3, command=lambda: soma())
  btn_soma.grid(column=0, row=0)
  btn_soma = tkinter.Button(grd_tela04, text="-", height = 3, width = 3, command=lambda: sub())
  btn_soma.grid(column=0, row=1)

  btn_soma = tkinter.Button(grd_tela04, text="=", height = 3, width = 3, command=lambda: tela("="))
  #btn_soma.grid(column=0, row=2)

  root.mainloop()
