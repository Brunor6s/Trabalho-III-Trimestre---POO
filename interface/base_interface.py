"""
Módulo base_interface - Interface base com menu lateral.

Define a estrutura comum para todas as interfaces de usuário com menu lateral.
"""

import tkinter as tk
from tkinter import ttk
from . import cores


class BaseInterface:
    """
    Classe base para interfaces com menu lateral.
    
    Fornece estrutura comum:
    - Menu lateral com informações do usuário
    - Área central para conteúdo
    - Botão de sair
    """
    
    def __init__(self, janela, usuario, on_logout):
        """
        Inicializa a interface base.
        
        Args:
            janela: Janela principal do Tkinter
            usuario: Dicionário com dados do usuário logado
            on_logout: Callback para quando usuário fizer logout
        """
        self.janela = janela
        self.usuario = usuario
        self.on_logout = on_logout
        self.aba_atual = None
        
        # Frame principal
        self.frame = tk.Frame(janela, bg=cores.FUNDO_CLARO)
        self.frame.pack(fill='both', expand=True)
        
        # Criar layout
        self._criar_menu_lateral()
        self._criar_area_conteudo()
    
    def _criar_menu_lateral(self):
        """Cria o menu lateral com navegação."""
        self.menu_frame = tk.Frame(self.frame,
                                   bg=cores.FUNDO_MENU,
                                   width=250)
        self.menu_frame.pack(side='left', fill='y')
        self.menu_frame.pack_propagate(False)
        
        # Cabeçalho do menu
        header = tk.Frame(self.menu_frame, bg=cores.PRIMARIA, height=100)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header,
                text="🏨 HOTEL SYSTEM",
                font=('Segoe UI', 14, 'bold'),
                bg=cores.PRIMARIA,
                fg=cores.TEXTO_CLARO).pack(pady=(20, 5))
        
        # Informações do usuário
        user_frame = tk.Frame(self.menu_frame, bg=cores.FUNDO_MENU, pady=20)
        user_frame.pack(fill='x', padx=15)
        
        tipo_usuario = self.usuario['tipo'].upper()
        tk.Label(user_frame,
                text=f"👤 {tipo_usuario}",
                font=('Segoe UI', 10, 'bold'),
                bg=cores.FUNDO_MENU,
                fg=cores.DESTAQUE).pack(anchor='w')
        
        tk.Label(user_frame,
                text=self.usuario['nome'],
                font=('Segoe UI', 11, 'bold'),
                bg=cores.FUNDO_MENU,
                fg=cores.TEXTO_CLARO).pack(anchor='w', pady=(5, 2))
        
        tk.Label(user_frame,
                text=self.usuario['email'],
                font=('Segoe UI', 9),
                bg=cores.FUNDO_MENU,
                fg=cores.TEXTO_SECUNDARIO).pack(anchor='w')
        
        # Separador
        tk.Frame(self.menu_frame,
                bg=cores.SECUNDARIA,
                height=2).pack(fill='x', pady=10)
        
        # Container para botões de navegação
        self.nav_frame = tk.Frame(self.menu_frame, bg=cores.FUNDO_MENU)
        self.nav_frame.pack(fill='both', expand=True, padx=10)
        
        # Botão de sair (no rodapé)
        footer = tk.Frame(self.menu_frame, bg=cores.FUNDO_MENU)
        footer.pack(side='bottom', fill='x', padx=10, pady=15)
        
        btn_sair = tk.Button(footer,
                            text="🚪 Sair",
                            font=('Segoe UI', 10, 'bold'),
                            bg=cores.ERRO,
                            fg=cores.TEXTO_CLARO,
                            activebackground='#C0392B',
                            activeforeground=cores.TEXTO_CLARO,
                            relief='flat',
                            cursor='hand2',
                            command=self._fazer_logout)
        btn_sair.pack(fill='x', ipady=10)
    
    def _criar_area_conteudo(self):
        """Cria a área central para exibição de conteúdo."""
        self.conteudo_frame = tk.Frame(self.frame, bg=cores.FUNDO_CLARO)
        self.conteudo_frame.pack(side='right', fill='both', expand=True)
    
    def adicionar_botao_menu(self, texto, icone, comando):
        """
        Adiciona um botão ao menu lateral.
        
        Args:
            texto: Texto do botão
            icone: Ícone emoji do botão
            comando: Função a ser executada ao clicar
        
        Returns:
            O botão criado
        """
        btn = tk.Button(self.nav_frame,
                       text=f"{icone}  {texto}",
                       font=('Segoe UI', 10),
                       bg=cores.FUNDO_MENU,
                       fg=cores.TEXTO_CLARO,
                       activebackground=cores.SECUNDARIA,
                       activeforeground=cores.TEXTO_CLARO,
                       relief='flat',
                       anchor='w',
                       padx=15,
                       cursor='hand2',
                       command=comando)
        btn.pack(fill='x', pady=2, ipady=10)
        return btn
    
    def limpar_conteudo(self):
        """Limpa o conteúdo da área central."""
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()
    
    def _fazer_logout(self):
        """Faz logout e retorna para tela de login."""
        self.frame.destroy()
        self.on_logout()
    
    def destruir(self):
        """Destrói a interface."""
        self.frame.destroy()