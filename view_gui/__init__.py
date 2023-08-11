from tkinter import *


def donothing():
    x = 0


def main():

    window = Tk()
    window.title("Programa de Investigação")
    window.geometry("600x500")
    menubar = Menu(window)
    window.config(menu=menubar)

    menu_cadastro(menubar, window)
    menu_configuracao(menubar)
    window.mainloop()


def menu_cadastro(master, window):
    menu = Menu(master, tearoff=0)

    menu.add_command(label="Abordado", command=(lambda: FrameCadastroAbordado(window)))
    menu.add_command(label="Abordagem", command=(lambda: None))
    menu.add_command(label="Boletim de Ocorrência", command=(lambda: None))
    menu.add_command(label="Local", command=(lambda: None))
    menu.add_command(label="Veículo", command=(lambda: None))
    master.add_cascade(label="Cadastro", menu=menu)


def menu_configuracao(master):
    menu = Menu(master, tearoff=0)

    menu.add_command(label="Banco de Dados", command=lambda: None)
    menu.add_command(label="Sobre", command=lambda: None)
    menu.add_separator()
    menu.add_command(label="Sair", command=lambda: None)
    master.add_cascade(label="Configuracao", menu=menu)


class FrameCadastroAbordado:

    def __init__(self, master):
        self.frame = Frame(master)

        Label(master, text="Nome:").pack()
        self.txt_abordado = Entry(master)
        self.txt_abordado.pack()

        Label(master, text="Apelido:").pack()
        self.txt_apelido = Entry(master)
        self.txt_apelido.pack()

        Label(master, text="RG:").pack()
        self.txt_rg = Entry(master)
        self.txt_rg.pack()

        Label(master, text="Foto:").pack()
        self.txt_foto = Entry(master)
        self.txt_foto.pack()

    def __dict__(self):
        return {
            "nome": self.txt_abordado.get(),
            "apelido": self.txt_apelido.get(),
            "rg": self.txt_rg.get()}