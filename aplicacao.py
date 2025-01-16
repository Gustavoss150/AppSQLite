from frontend import *
import backend as core

# variáveis globais
app = None
selected = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)

    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)

    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())

    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    global selected
    if selected:  # Verifica se um item foi selecionado
        core.update(
            int(selected[0]),  # Certifique-se de converter o ID para inteiro
            app.entNome.get(),
            app.entSobrenome.get(),
            app.entEmail.get(),
            app.entCPF.get()
        )
        view_command()  # Atualiza a lista após atualizar
    else:
        print("Nenhum item selecionado para atualização.")

def del_command():
    global selected
    if selected:  # Verifica se um item foi selecionado
        id = int(selected[0])  # Garante que seja um inteiro
        core.delete(id)
        view_command()
    else:
        print("Nenhum item selecionado para exclusão.")

def getSelectedRow(event):
    global selected
    if not app.listClientes.curselection():
        return
    
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)

    if selected:
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])

        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])

        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])


if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)  # Corrigido evento para 'ListboxSelect'

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
