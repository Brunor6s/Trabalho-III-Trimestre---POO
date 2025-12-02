"""
Módulo login - Tela de login do sistema.

Implementa a tela inicial com autenticação de usuários (Dono, Funcionário, Cliente).
"""

import tkinter as tk
from tkinter import ttk, messagebox
from . import cores


class TelaLogin:
    """
    Tela de login do sistema.
    
    Permite autenticação de três tipos de usuários:
    - Dono (credenciais fixas)
    - Funcionário (cadastrado no sistema)
    - Cliente (cadastrado no sistema)
    """
    
    def __init__(self, janela, cliente_service, funcionario_service, on_login_success):
        """
        Inicializa a tela de login.
        
        Args:
            janela: Janela principal do Tkinter
            cliente_service: Serviço de gerenciamento de clientes
            funcionario_service: Serviço de gerenciamento de funcionários
            on_login_success: Callback chamado quando login é bem-sucedido
        """
        self.janela = janela
        self.cliente_service = cliente_service
        self.funcionario_service = funcionario_service
        self.on_login_success = on_login_success
        
        # Frame principal
        self.frame = tk.Frame(janela, bg=cores.FUNDO_CLARO)
        self.frame.pack(fill='both', expand=True)
        
        self._criar_interface()
    
    def _criar_interface(self):
        """Cria os componentes da interface de login."""
        # Container centralizado
        container = tk.Frame(self.frame, bg=cores.FUNDO_CLARO)
        container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Logo/Título do sistema
        titulo_frame = tk.Frame(container, bg=cores.PRIMARIA, padx=40, pady=20)
        titulo_frame.pack(fill='x', pady=(0, 30))
        
        tk.Label(titulo_frame,
                text="🏨 SISTEMA DE HOTEL",
                font=('Segoe UI', 24, 'bold'),
                bg=cores.PRIMARIA,
                fg=cores.TEXTO_CLARO).pack()
        
        tk.Label(titulo_frame,
                text="Gestão de Reservas",
                font=('Segoe UI', 12),
                bg=cores.PRIMARIA,
                fg=cores.TEXTO_CLARO).pack()
        
        # Card de login
        card = tk.Frame(container, bg='white', padx=40, pady=30)
        card.pack(fill='both', expand=True)
        
        # Título do card
        tk.Label(card,
                text="Entrar no Sistema",
                font=('Segoe UI', 16, 'bold'),
                bg='white',
                fg=cores.TEXTO_ESCURO).pack(pady=(0, 20))
        
        # Campo Email
        tk.Label(card,
                text="Email:",
                font=('Segoe UI', 10),
                bg='white',
                fg=cores.TEXTO_ESCURO,
                anchor='w').pack(fill='x', pady=(0, 5))
        
        self.email_entry = tk.Entry(card,
                                    font=('Segoe UI', 11),
                                    bg=cores.INPUT_FUNDO,
                                    fg=cores.TEXTO_ESCURO,
                                    relief='solid',
                                    borderwidth=1)
        self.email_entry.pack(fill='x', ipady=8, pady=(0, 15))
        self.email_entry.focus()
        
        # Campo Senha
        tk.Label(card,
                text="Senha:",
                font=('Segoe UI', 10),
                bg='white',
                fg=cores.TEXTO_ESCURO,
                anchor='w').pack(fill='x', pady=(0, 5))
        
        self.senha_entry = tk.Entry(card,
                                    font=('Segoe UI', 11),
                                    bg=cores.INPUT_FUNDO,
                                    fg=cores.TEXTO_ESCURO,
                                    relief='solid',
                                    borderwidth=1,
                                    show='•')
        self.senha_entry.pack(fill='x', ipady=8, pady=(0, 25))
        
        # Bind Enter para login
        self.email_entry.bind('<Return>', lambda e: self._fazer_login())
        self.senha_entry.bind('<Return>', lambda e: self._fazer_login())
        
        # Botão de login
        btn_login = tk.Button(card,
                             text="ENTRAR",
                             font=('Segoe UI', 11, 'bold'),
                             bg=cores.BOTAO_NORMAL,
                             fg=cores.TEXTO_CLARO,
                             activebackground=cores.BOTAO_HOVER,
                             activeforeground=cores.TEXTO_CLARO,
                             relief='flat',
                             cursor='hand2',
                             command=self._fazer_login)
        btn_login.pack(fill='x', ipady=10)
    
    def _fazer_login(self):
        """Processa o login do usuário."""
        email = self.email_entry.get().strip()
        senha = self.senha_entry.get()
        
        if not email or not senha:
            messagebox.showerror("Erro", "Por favor, preencha email e senha.")
            return
        
        usuario = None
        
        # Verificar dono (credenciais fixas)
        if (email == "maria.jobim@habbo.com" or email == "dono") and senha == "habbohotel2025":
            usuario = {
                "tipo": "dono",
                "nome": "Administrador",
                "email": "maria.jobim@habbo.com"
            }
        
        # Verificar funcionário
        if not usuario:
            func = self.funcionario_service.buscarPorEmail(email)
            if func and func.senha == senha:
                usuario = {
                    "tipo": "funcionario",
                    "nome": func.nome,
                    "email": func.email,
                    "objeto": func
                }
        
        # Verificar cliente
        if not usuario:
            cliente = self.cliente_service.buscarPorEmail(email)
            if cliente and cliente.senha == senha:
                usuario = {
                    "tipo": "cliente",
                    "nome": cliente.nome,
                    "email": cliente.email,
                    "objeto": cliente
                }
        
        if usuario:
            self.frame.destroy()
            self.on_login_success(usuario)
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos.")
            self.senha_entry.delete(0, 'end')
            self.senha_entry.focus()
    
    def destruir(self):
        """Destrói a tela de login."""
        self.frame.destroy()
