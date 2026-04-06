import tkinter as tk
from tkinter import filedialog

def criar_novo_arquivo(bloco_texto):
    bloco_texto.delete(1.0, tk.END)
    bloco_texto.arquivo_atual = None

def salvar_arquivo(bloco_texto):
    if bloco_texto.arquivo_atual:
        with open(bloco_texto.arquivo_atual, 'w') as arquivo:
            arquivo.write(bloco_texto.get(1.0, tk.END))
    else:
        salvar_arquivo_como(bloco_texto)


def salvar_arquivo_como(bloco_texto):
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if caminho_arquivo:
        bloco_texto.arquivo_atual = caminho_arquivo
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(bloco_texto.get(1.0, tk.END))

def abrir_arquivo(bloco_texto):
    caminho_arquivo = filedialog.askopenfilename()
    if caminho_arquivo:
        bloco_texto.arquivo_atual = caminho_arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            bloco_texto.delete(1.0, tk.END)
            bloco_texto.insert(tk.END, arquivo.read())