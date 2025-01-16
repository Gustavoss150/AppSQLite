from tkinter import *

class Gui:  # Classe da interface gráfica
    def __init__(self):
        # Criar uma janela
        self.window = Tk()
        self.window.title("PYSQL versão 1.0")

        # Padding e largura das entradas
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30  # Define a largura dos campos de entrada

        # Definição das variáveis que recebem os dados inseridos pelo usuário
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels
        Label(self.window, text="Nome").grid(row=0, column=0, padx=self.x_pad, pady=self.y_pad)
        Label(self.window, text="Sobrenome").grid(row=1, column=0, padx=self.x_pad, pady=self.y_pad)
        Label(self.window, text="Email").grid(row=2, column=0, padx=self.x_pad, pady=self.y_pad)
        Label(self.window, text="CPF").grid(row=3, column=0, padx=self.x_pad, pady=self.y_pad)

        # Campos de entrada (Entry)
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entNome.grid(row=0, column=1, padx=self.x_pad, pady=self.y_pad)

        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entSobrenome.grid(row=1, column=1, padx=self.x_pad, pady=self.y_pad)

        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entEmail.grid(row=2, column=1, padx=self.x_pad, pady=self.y_pad)

        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)
        self.entCPF.grid(row=3, column=1, padx=self.x_pad, pady=self.y_pad)

        # Lista e Scrollbar
        self.listClientes = Listbox(self.window, width=100)
        self.listClientes.grid(row=4, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad)

        self.scrollClientes = Scrollbar(self.window)
        self.scrollClientes.grid(row=4, column=2, sticky='ns')

        # Vincular Scrollbar à Listbox
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Botões
        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnViewAll.grid(row=5, column=0, padx=self.x_pad, pady=self.y_pad)

        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnBuscar.grid(row=5, column=1, padx=self.x_pad, pady=self.y_pad)

        self.btnInserir = Button(self.window, text="Inserir")
        self.btnInserir.grid(row=6, column=0, padx=self.x_pad, pady=self.y_pad)

        self.btnUpdate = Button(self.window, text="Atualizar Selecionado")
        self.btnUpdate.grid(row=6, column=1, padx=self.x_pad, pady=self.y_pad)

        self.btnDel = Button(self.window, text="Deletar Selecionado")
        self.btnDel.grid(row=7, column=0, padx=self.x_pad, pady=self.y_pad)

        self.btnClose = Button(self.window, text="Fechar", command=self.window.quit)
        self.btnClose.grid(row=7, column=1, padx=self.x_pad, pady=self.y_pad)

        # Adicionar SWAG (aparência) à interface
        self.apply_styles()

    def apply_styles(self):
        """ Aplica estilos aos elementos da interface """
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        """ Executa o loop principal da interface """
        self.window.mainloop()
