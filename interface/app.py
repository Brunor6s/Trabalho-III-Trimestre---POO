"""
Módulo app - Aplicação principal do sistema.

Gerencia a janela principal e a troca entre telas (login e interfaces de usuário).
"""

import tkinter as tk
from .login import TelaLogin
from .interface_dono import InterfaceDono
from .interface_funcionario import InterfaceFuncionario
from .interface_cliente import InterfaceCliente
from .estilos import configurar_estilos


class HotelApp:
    """
    Aplicação principal do sistema de hotel.
    
    Gerencia a janela principal e a navegação entre diferentes interfaces.
    """
    
    def __init__(self, cliente_service, funcionario_service, quarto_service, reserva_service):
        """
        Inicializa a aplicação.
        
        Args:
            cliente_service: Serviço de gerenciamento de clientes
            funcionario_service: Serviço de gerenciamento de funcionários
            quarto_service: Serviço de gerenciamento de quartos
            reserva_service: Serviço de gerenciamento de reservas
        """
        # Armazenar services
        self.services = {
            'cliente': cliente_service,
            'funcionario': funcionario_service,
            'quarto': quarto_service,
            'reserva': reserva_service
        }
        
        # Criar janela principal
        self.janela = tk.Tk()
        self.janela.title("Sistema de Hotel - Gestão de Reservas")
        
        # Abrir em tela cheia
        self.janela.state('zoomed')
        
        # Configurar estilos
        configurar_estilos()
        
        # Interface atual
        self.interface_atual = None
        
        # Mostrar tela de login
        self.mostrar_login()
    
    def mostrar_login(self):
        """Exibe a tela de login."""
        if self.interface_atual:
            self.interface_atual.destruir()
        
        self.interface_atual = TelaLogin(
            self.janela,
            self.services['cliente'],
            self.services['funcionario'],
            self.on_login_success
        )
    
    def on_login_success(self, usuario):
        """
        Callback chamado quando login é bem-sucedido.
        
        Args:
            usuario: Dicionário com dados do usuário logado
        """
        # Destruir tela de login
        if self.interface_atual:
            self.interface_atual.destruir()
        
        # Criar interface apropriada baseada no tipo de usuário
        tipo = usuario['tipo']
        
        if tipo == 'dono':
            self.interface_atual = InterfaceDono(
                self.janela,
                usuario,
                self.services,
                self.mostrar_login
            )
        elif tipo == 'funcionario':
            self.interface_atual = InterfaceFuncionario(
                self.janela,
                usuario,
                self.services,
                self.mostrar_login
            )
        elif tipo == 'cliente':
            self.interface_atual = InterfaceCliente(
                self.janela,
                usuario,
                self.services,
                self.mostrar_login
            )
    
    def run(self):
        """Inicia o loop principal da aplicação."""
        self.janela.mainloop()
