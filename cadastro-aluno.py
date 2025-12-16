import tkinter as tk
from tkinter import ttk



def adicional_alunos():
    name = entry_name.get()
    email = entry_email.get()
    
    tree.insert('', tk.END, values=(name, email))
    entry_name.delete(0 , tk.END)
    entry_email.delete(0,tk.END)
    

root =tk.Tk()
root.title("Cadastro de Alunos")
root.configure(bg="#F5F5F5") # muda o fundo

tree = ttk.Treeview(root, columns=("Nome", "Email"))
tree.heading("Nome", text=" Nome")
tree.heading("Email", text=" Email")
tree.pack()



label_name = tk.Label(root, text="Name")
label_name.pack(pady=2)
entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="E-mail")
label_email.pack(pady=2)
entry_email = tk.Entry(root)
entry_email.pack()

# ===== BOTÃO =====
btn_add = tk.Button(
    root,
    text="Adicionar",
    bg="#4CAF50",   # cor de fundo
    fg="white",
    width=15,
    command= adicional_alunos
)
btn_add.pack(pady=15)





root.update()  # força a atualização da interface gráfica
root.mainloop() # Mantém a janela aberta
