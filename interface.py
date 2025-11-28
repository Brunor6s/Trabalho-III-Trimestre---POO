import tkinter as tk
from tkinter import messagebox

class Interface:

    def __init__(self, serv_cliente, serv_funcionario, serv_quarto):
        self.clienteService = serv_cliente
        self.funcService = serv_funcionario
        self.quartoService = serv_quarto
        self.usuario_logado = None

        self.janela = tk.Tk()
        self.janela.title("Sistema de Hotel")
        self.janela.geometry("400x400")

    # ===============================
    # CONTROLADOR DE TELA
    # ===============================
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    # ===============================
    # TELA LOGIN
    # ===============================
    def tela_login(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Email:").pack()
        email = tk.Entry(self.janela)
        email.pack()

        tk.Label(self.janela, text="Senha:").pack()
        senha = tk.Entry(self.janela, show="*")
        senha.pack()

        def entrar():
            em = email.get()
            pw = senha.get()
            usuario = None

            # DONO fixo
            if em == "dono" and pw == "123":
                usuario = {"tipo": "dono", "nome": "Dono"}

            # FUNCIONÁRIO
            for f in self.funcService.funcionarios:
                if f.email == em and f.senha == pw:
                    usuario = {"tipo": "func", "nome": f.nome}

            # CLIENTE
            for c in self.clienteService.clientes:
                if c.email == em and c.senha == pw:
                    usuario = {"tipo": "cliente", "nome": c.nome}

            if usuario:
                self.usuario_logado = usuario
                if usuario["tipo"] == "dono":
                    self.menu_dono()
                elif usuario["tipo"] == "func":
                    self.menu_func()
                else:
                    self.menu_cliente()
            else:
                messagebox.showerror("Erro", "Credenciais inválidas.")

        tk.Button(self.janela, text="Entrar", command=entrar).pack(pady=10)

    # ===============================
    # MENUS
    # ===============================
    def menu_dono(self):
        self.limpar_tela()
        tk.Label(self.janela, text="Menu Dono", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.janela, text="Cadastrar Cliente", command=self.tela_cadastrar_cliente).pack(pady=4)
        tk.Button(self.janela, text="Cadastrar Funcionário", command=self.tela_cadastrar_funcionario).pack(pady=4)
        tk.Button(self.janela, text="Cadastrar Quarto", command=self.tela_cadastrar_quarto).pack(pady=4)

        tk.Button(self.janela, text="Listar Clientes", command=self.listar_clientes).pack(pady=4)
        tk.Button(self.janela, text="Listar Funcionários", command=self.listar_funcionarios).pack(pady=4)
        tk.Button(self.janela, text="Listar Quartos", command=self.listar_quartos).pack(pady=4)

        tk.Button(self.janela, text="Sair", command=self.tela_login).pack(pady=10)

    def menu_func(self):
        self.limpar_tela()
        tk.Label(self.janela, text="Menu Funcionário", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.janela, text="Cadastrar Cliente", command=self.tela_cadastrar_cliente).pack(pady=4)
        tk.Button(self.janela, text="Listar Clientes", command=self.listar_clientes).pack(pady=4)
        tk.Button(self.janela, text="Listar Quartos", command=self.listar_quartos).pack(pady=4)

        tk.Button(self.janela, text="Sair", command=self.tela_login).pack(pady=10)

    def menu_cliente(self):
        self.limpar_tela()
        tk.Label(self.janela, text="Menu Cliente", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.janela, text="Listar Quartos", command=self.listar_quartos).pack(pady=4)

        tk.Button(self.janela, text="Sair", command=self.tela_login).pack(pady=10)

    # ===============================
    # CADASTRAR CLIENTE
    # ===============================
    def tela_cadastrar_cliente(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Cadastrar Cliente", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Nome:").pack()
        nome = tk.Entry(self.janela)
        nome.pack()

        tk.Label(self.janela, text="Email:").pack()
        email = tk.Entry(self.janela)
        email.pack()

        tk.Label(self.janela, text="Senha:").pack()
        senha = tk.Entry(self.janela, show="*")
        senha.pack()

        tk.Label(self.janela, text="CPF (11 dígitos):").pack()
        cpf = tk.Entry(self.janela)
        cpf.pack()

        def salvar():
            if len(cpf.get()) != 11:
                messagebox.showerror("Erro", "CPF deve ter 11 dígitos.")
                return

            novo = self.clienteService.criar(nome.get(), cpf.get(), email.get(), senha.get())
            messagebox.showinfo("OK", "Cliente cadastrado!")

            if self.usuario_logado["tipo"] == "dono":
                self.menu_dono()
            else:
                self.menu_func()

        tk.Button(self.janela, text="Salvar", command=salvar).pack(pady=10)
        tk.Button(self.janela, text="Voltar", command=self.menu_dono if self.usuario_logado["tipo"]=="dono" else self.menu_func).pack()

    # ===============================
    # CADASTRAR FUNCIONÁRIO
    # ===============================
    def tela_cadastrar_funcionario(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Cadastrar Funcionário", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Nome:").pack()
        nome = tk.Entry(self.janela)
        nome.pack()

        tk.Label(self.janela, text="Email:").pack()
        email = tk.Entry(self.janela)
        email.pack()

        tk.Label(self.janela, text="Senha:").pack()
        senha = tk.Entry(self.janela, show="*")
        senha.pack()

        def salvar():
            self.funcService.criar(nome.get(), email.get(), senha.get())
            messagebox.showinfo("OK", "Funcionário cadastrado!")
            self.menu_dono()

        tk.Button(self.janela, text="Salvar", command=salvar).pack(pady=10)
        tk.Button(self.janela, text="Voltar", command=self.menu_dono).pack()

    # ===============================
    # CADASTRAR QUARTO
    # ===============================
    def tela_cadastrar_quarto(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Cadastrar Quarto", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.janela, text="Número do Quarto:").pack()
        numero = tk.Entry(self.janela)
        numero.pack()

        tk.Label(self.janela, text="Preço:").pack()
        preco = tk.Entry(self.janela)
        preco.pack()

        def salvar():
            self.quartoService.criar(numero.get(), preco.get())
            messagebox.showinfo("OK", "Quarto cadastrado!")
            self.menu_dono()

        tk.Button(self.janela, text="Salvar", command=salvar).pack(pady=10)
        tk.Button(self.janela, text="Voltar", command=self.menu_dono).pack()

    # ===============================
    # LISTAGENS
    # ===============================
    def listar_clientes(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Clientes", font=("Arial", 16)).pack(pady=10)

        for c in self.clienteService.clientes:
            tk.Label(self.janela, text=f"{c.nome} - {c.email} - CPF: {c.cpf}").pack()

        tk.Button(self.janela, text="Voltar",
                  command=self.menu_dono if self.usuario_logado["tipo"]=="dono" else self.menu_func).pack(pady=10)

    def listar_funcionarios(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Funcionários", font=("Arial", 16)).pack(pady=10)

        for f in self.funcService.funcionarios:
            tk.Label(self.janela, text=f"{f.nome} - {f.email}").pack()

        tk.Button(self.janela, text="Voltar", command=self.menu_dono).pack(pady=10)

    def listar_quartos(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Quartos", font=("Arial", 16)).pack(pady=10)

        for q in self.quartoService.quartos:
            tk.Label(self.janela, text=f"Quarto {q.numero} - R$ {q.preco}").pack()

        tk.Button(self.janela, text="Voltar",
                  command=self.menu_dono if self.usuario_logado["tipo"]=="dono" else self.menu_func).pack(pady=10)

    # ===============================
    # EXECUTAR
    # ===============================
    def run(self):
        self.tela_login()
        self.janela.mainloop()
