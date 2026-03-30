"""
Módulo estilos - Configuração visual dos componentes da interface.
"""
import tkinter as tk
from tkinter import ttk
from . import cores

def configurar_estilos():
    """Configura o tema e os estilos dos widgets ttk."""
    style = ttk.Style()
    
    # Estilo da Tabela (Treeview)
    style.theme_use('clam')
    
    style.configure("Modern.Treeview",
                    background="white",
                    foreground=cores.TEXTO_ESCURO,
                    rowheight=35,
                    fieldbackground="white",
                    font=('Segoe UI', 10))
    
    style.configure("Modern.Treeview.Heading",
                    background=cores.TABELA_HEADER,
                    foreground="white",
                    font=('Segoe UI', 10, 'bold'),
                    relief='flat')
    
    style.map("Modern.Treeview",
              background=[('selected', cores.DESTAQUE)])

    # Estilo para Combobox
    style.configure("TCombobox", padding=5)