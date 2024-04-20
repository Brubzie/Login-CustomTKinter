import customtkinter as ctk
from tkinter import messagebox

def check_login():
    if username_entry.get() == 'admin' and password_entry.get() == 'password':
        messagebox.showinfo('Login realizado com sucesso', 'Seja bem-vindo Admin!')
    elif username_entry.get() != 'admin' and password_entry.get() != 'password':
        messagebox.showinfo('Login realizado com sucesso', f'Seja bem-vindo {username_entry.get()}!')
    else:
        messagebox.showerror('Falha no login', 'Usuário ou senha inválido(s)')

root = ctk.CTk()

username_label = ctk.CTkLabel(root, text = 'Nome de usuário')
username_label.pack(pady = (10, 0))

username_entry = ctk.CTkEntry(root)
username_entry.pack(pady = (0, 10))

password_label = ctk.CTkLabel(root, text = 'Senha')
password_label.pack(pady = (10, 0))

password_entry = ctk.CTkEntry(root, show = '*')
password_entry.pack(pady = (0, 10))

login_button = ctk.CTkButton(root, text = 'Login', command = check_login)
login_button.pack(pady = 10)

root.mainloop()
