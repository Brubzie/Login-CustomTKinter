import customtkinter as ctk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x200')  # Definindo um tamanho mínimo para a janela

        self.username_label = ctk.CTkLabel(self.root, text = 'Nome de usuário')
        self.username_label.pack(pady = (10, 0))

        self.username_entry = ctk.CTkEntry(self.root)
        self.username_entry.pack(pady = (0, 10))

        self.password_label = ctk.CTkLabel(self.root, text = 'Senha')
        self.password_label.pack(pady = (10, 0))

        self.password_entry = ctk.CTkEntry(self.root, show = '*')
        self.password_entry.pack(pady = (0, 10))

        self.login_button = ctk.CTkButton(self.root, text = 'Login', command = self.check_login)
        self.login_button.pack(pady = 10)

    def check_login(self):
        username = self.username_entry.get().strip()  # Removendo espaços em branco no início e no final
        password = self.password_entry.get()

        if len(password) < 8:
            messagebox.showerror('Falha no login', 'A senha deve ter pelo menos 8 caracteres')
        elif username == 'admin' and password == 'password':
            messagebox.showinfo('Login realizado com sucesso', 'Seja bem-vindo Admin!')
        elif username != 'admin' and password != 'password':
            messagebox.showinfo('Login realizado com sucesso', f'Seja bem-vindo {username}!')
        else:
            messagebox.showerror('Falha no login', 'Usuário ou senha inválido(s)')

root = ctk.CTk()
app = LoginWindow(root)
root.mainloop()
