"""
Módulo componentes - Componentes reutilizáveis da interface.

Fornece widgets customizados para formulários, tabelas e outros elementos comuns.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from . import cores


class FormularioBase:
    """Classe base para criar formulários."""
    
    def __init__(self, parent):
        """
        Inicializa o formulário.
        
        Args:
            parent: Widget pai onde o formulário será inserido
        """
        self.parent = parent
        self.campos = {}
        self.frame = tk.Frame(parent, bg='white', padx=30, pady=20)
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)
    
    def adicionar_campo(self, nome, label, tipo='text', opcoes=None, linha=None):
        """
        Adiciona um campo ao formulário.
        
        Args:
            nome: Nome identificador do campo
            label: Texto do rótulo
            tipo: Tipo do campo ('text', 'password', 'combo')
            opcoes: Lista de opções (para tipo 'combo')
            linha: Linha específica para posicionar (opcional)
        
        Returns:
            O widget de entrada criado
        """
        # Label
        tk.Label(self.frame,
                text=label + ":",
                font=('Segoe UI', 10),
                bg='white',
                fg=cores.TEXTO_ESCURO,
                anchor='w').pack(fill='x', pady=(10, 5))
        
        # Campo de entrada
        if tipo == 'combo':
            campo = ttk.Combobox(self.frame,
                                font=('Segoe UI', 10),
                                state='readonly')
            if opcoes:
                campo['values'] = opcoes
                campo.set(opcoes[0] if opcoes else '')
        elif tipo == 'password':
            campo = tk.Entry(self.frame,
                            font=('Segoe UI', 10),
                            bg=cores.INPUT_FUNDO,
                            fg=cores.TEXTO_ESCURO,
                            relief='solid',
                            borderwidth=1,
                            show='•')
        else:  # text
            campo = tk.Entry(self.frame,
                            font=('Segoe UI', 10),
                            bg=cores.INPUT_FUNDO,
                            fg=cores.TEXTO_ESCURO,
                            relief='solid',
                            borderwidth=1)
        
        campo.pack(fill='x', ipady=8)
        self.campos[nome] = campo
        return campo
    
    def obter_valores(self):
        """
        Obtém todos os valores dos campos do formulário.
        
        Returns:
            Dicionário com nome do campo: valor
        """
        valores = {}
        for nome, campo in self.campos.items():
            if isinstance(campo, ttk.Combobox):
                valores[nome] = campo.get()
            else:
                valores[nome] = campo.get().strip()
        return valores
    
    def limpar(self):
        """Limpa todos os campos do formulário."""
        for campo in self.campos.values():
            if isinstance(campo, ttk.Combobox):
                campo.set('')
            else:
                campo.delete(0, 'end')
    
    def adicionar_botoes(self, botoes):
        """
        Adiciona botões ao formulário.
        
        Args:
            botoes: Lista de tuplas (texto, comando, estilo)
        """
        btn_frame = tk.Frame(self.frame, bg='white')
        btn_frame.pack(fill='x', pady=(20, 0))
        
        for texto, comando, estilo in botoes:
            cor_bg = cores.SUCESSO if estilo == 'success' else cores.BOTAO_NORMAL
            cor_hover = '#229954' if estilo == 'success' else cores.BOTAO_HOVER
            
            btn = tk.Button(btn_frame,
                           text=texto,
                           font=('Segoe UI', 10, 'bold'),
                           bg=cor_bg,
                           fg=cores.TEXTO_CLARO,
                           activebackground=cor_hover,
                           activeforeground=cores.TEXTO_CLARO,
                           relief='flat',
                           cursor='hand2',
                           command=comando)
            btn.pack(side='left', padx=5, ipady=10, ipadx=20)


class TabelaModerna:
    """Componente de tabela moderna com Treeview."""
    
    def __init__(self, parent, colunas, larguras=None):
        """
        Inicializa a tabela.
        
        Args:
            parent: Widget pai
            colunas: Lista de tuplas (id, título) das colunas
            larguras: Dicionário com largura de cada coluna
        """
        self.parent = parent
        self.colunas = colunas
        
        # Frame container
        self.frame = tk.Frame(parent, bg='white')
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Criar Treeview com scrollbar
        self._criar_treeview(larguras)
    
    def _criar_treeview(self, larguras):
        """Cria o widget Treeview com scrollbar."""
        # Container com scrollbar
        container = tk.Frame(self.frame, bg='white')
        container.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(container, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        # Treeview
        cols = [col[0] for col in self.colunas]
        self.tree = ttk.Treeview(container,
                                columns=cols,
                                show='headings',
                                yscrollcommand=scrollbar.set,
                                style='Modern.Treeview')
        self.tree.pack(side='left', fill='both', expand=True)
        
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        for col_id, col_titulo in self.colunas:
            self.tree.heading(col_id, text=col_titulo)
            largura = larguras.get(col_id, 150) if larguras else 150
            self.tree.column(col_id, width=largura, anchor='center')
    
    def limpar(self):
        """Remove todos os itens da tabela."""
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def adicionar_item(self, valores):
        """
        Adiciona um item à tabela.
        
        Args:
            valores: Tupla com valores de cada coluna
        """
        self.tree.insert('', 'end', values=valores)
    
    def obter_selecionado(self):
        """
        Obtém o item selecionado.
        
        Returns:
            Tupla com valores do item selecionado ou None
        """
        selecionados = self.tree.selection()
        if selecionados:
            item = selecionados[0]
            return self.tree.item(item)['values']
        return None
    
    def obter_todos_itens(self):
        """
        Obtém todos os itens da tabela.
        
        Returns:
            Lista de tuplas com valores de cada item
        """
        itens = []
        for item in self.tree.get_children():
            itens.append(self.tree.item(item)['values'])
        return itens


def criar_titulo_pagina(parent, titulo, subtitulo=None):
    """
    Cria um título de página padronizado.
    
    Args:
        parent: Widget pai
        titulo: Texto do título principal
        subtitulo: Texto do subtítulo (opcional)
    
    Returns:
        Frame contendo o título
    """
    frame = tk.Frame(parent, bg=cores.FUNDO_CLARO, pady=20)
    frame.pack(fill='x', padx=20)
    
    tk.Label(frame,
            text=titulo,
            font=('Segoe UI', 20, 'bold'),
            bg=cores.FUNDO_CLARO,
            fg=cores.TEXTO_ESCURO).pack(anchor='w')
    
    if subtitulo:
        tk.Label(frame,
                text=subtitulo,
                font=('Segoe UI', 11),
                bg=cores.FUNDO_CLARO,
                fg=cores.TEXTO_SECUNDARIO).pack(anchor='w', pady=(5, 0))
    
    # Linha separadora
    tk.Frame(frame,
            bg=cores.DESTAQUE,
            height=3).pack(fill='x', pady=(10, 0))
    
    return frame


def mostrar_mensagem_sucesso(mensagem):
    """Exibe mensagem de sucesso."""
    messagebox.showinfo("Sucesso", mensagem)


def mostrar_mensagem_erro(mensagem):
    """Exibe mensagem de erro."""
    messagebox.showerror("Erro", mensagem)


def confirmar_acao(mensagem):
    """
    Solicita confirmação do usuário.
    
    Args:
        mensagem: Mensagem de confirmação
    
    Returns:
        True se confirmado, False caso contrário
    """
    return messagebox.askyesno("Confirmar", mensagem)
