# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
import funcoes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Notepad - PyUIbuilder")
main.config(bg="#E4E2E2")
main.geometry("700x345")
main.update_idletasks()

screen_w = main.winfo_screenwidth()
screen_h = main.winfo_screenheight()
main_w = main.winfo_width()
main_h = main.winfo_height()

geometryX = (screen_w // 2) - (main_w // 2)
geometryY = (screen_h // 2) - (main_h // 2)

main.geometry("+%d+%d"%(geometryX, geometryY))

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: funcoes.criar_novo_arquivo(txtnotas))
menu_0.add_command(label="Open", command=lambda: funcoes.abrir_arquivo(txtnotas))
menu_0.add_command(label="Save", command=lambda: funcoes.salvar_arquivo(txtnotas))
menu_0.add_command(label="Save as", command=lambda: funcoes.salvar_arquivo_como(txtnotas))
menu.add_cascade(label="File", menu=menu_0)

menu_1 = tk.Menu(menu, tearoff=0)
menu_1.add_command(label="New Item", command=lambda: print("New Item clicked"))
menu.add_cascade(label="Edit", menu=menu_1)

txtnotas = tk.Text(master=main)
txtnotas.config(bg="#fff", fg="#000", font=("System", 13))
txtnotas.place(x=1, y=0, width=700, height=351)


main.mainloop()