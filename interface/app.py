"""
Módulo app - Aplicação principal do sistema de hotel.
Gerencia a janela principal e a troca entre as interfaces de usuário.
"""
import tkinter as tk
from .login import TelaLogin
from .interface_dono import InterfaceDono
from .interface_funcionario import InterfaceFuncionario
from .interface_cliente import InterfaceCliente
from .estilos import configurar_estilos

class HotelApp:
    """
    Classe principal que coordena o fluxo da aplicação.
    """
    
    def __init__(self, cliente_service, funcionario_service, quarto_service, reserva_service, financeiro_service):
        """
        Inicializa o App com todos os serviços necessários (DIP).
        """
        # Armazenar referências dos serviços
        self.services = {
            'cliente': cliente_service,
            'funcionario': funcionario_service,
            'quarto': quarto_service,
            'reserva': reserva_service,
            'financeiro': financeiro_service
        }
        
        # Configuração da Janela Principal
        self.janela = tk.Tk()
        self.janela.title("🏨 Hotel Management System - SOLID Edition")
        
        # Tenta abrir em tela cheia (Windows/Linux)
        try:
            self.janela.state('zoomed')
        except:
            self.janela.attributes('-fullscreen', True)
        
        # Aplicar Estilos Visuais
        configurar_estilos()
        
        self.interface_atual = None
        self.mostrar_login()
    
    def mostrar_login(self):
        """Limpa a tela e exibe o formulário de login."""
        if self.interface_atual:
            self.interface_atual.destruir()
        
        self.interface_atual = TelaLogin(
            self.janela,
            self.services['cliente'],
            self.services['funcionario'],
            self.on_login_success
        )
    
    def on_login_success(self, usuario):
        """Callback acionado após login válido."""
        if self.interface_atual:
            self.interface_atual.destruir()
        
        tipo = usuario['tipo']
        
        # Injeção de dependências nas interfaces específicas
        if tipo == 'dono':
            self.interface_atual = InterfaceDono(self.janela, usuario, self.services, self.mostrar_login)
        elif tipo == 'funcionario':
            self.interface_atual = InterfaceFuncionario(self.janela, usuario, self.services, self.mostrar_login)
        elif tipo == 'cliente':
            self.interface_atual = InterfaceCliente(self.janela, usuario, self.services, self.mostrar_login)
    
    def run(self):
        """Inicia o loop de eventos do Tkinter."""
        self.janela.mainloop()