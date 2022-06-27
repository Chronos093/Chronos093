from tkinter import *
from tkinter import ttk
from tkinter import Tk, RIGHT

root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

root.geometry("%dx%d" %(monitor_width, monitor_height))

btnSair = ttk.Button(root, command=root.destroy, text="SAIR")
btnSair.place(x=50, y=60)
  
print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))
root.mainloop()