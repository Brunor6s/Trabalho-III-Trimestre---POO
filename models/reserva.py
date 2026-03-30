"""
Módulo reserva - Define a classe Reserva do sistema de hotel.

Este módulo foi adaptado para o Princípio de Responsabilidade Única (SRP).
A classe agora foca exclusivamente na gestão do contrato de reserva, 
delegando cálculos financeiros complexos para serviços especializados.
"""

from datetime import date
from typing import TYPE_CHECKING

# Evita importação circular para fins de tipagem
if TYPE_CHECKING:
    from .cliente import Cliente
    from .quarto import Quarto


class Reserva:
    """
    Classe que representa uma reserva de quarto no hotel.
    
    Demonstra composição: uma Reserva possui um Cliente e um Quarto.
    Aplica o Princípio SRP: A classe é responsável apenas pelos dados e 
    pelo estado do ciclo de vida da reserva (Check-in/Check-out/Cancelamento).
    
    Atributos:
        idReserva (int): Identificador único da reserva gerado automaticamente.
        dataCheckin (date): Data de entrada do cliente no hotel.
        dataCheckout (date): Data prevista de saída do cliente.
        valorTotal (float): Valor final da fatura (atribuído via FinanceiroService).
        cliente (Cliente): Objeto da classe Cliente associado à reserva.
        quarto (Quarto): Objeto da classe Quarto associado à reserva.
    """
    
    # Atributo de classe para controle de ID único
    _contador_id = 0
    
    def __init__(self, dataCheckin: date, dataCheckout: date, cliente: 'Cliente', quarto: 'Quarto', idReserva: int = None):
        """
        Inicializa uma nova instância de Reserva com validações de integridade.
        
        Args:
            dataCheckin (date): Data de entrada.
            dataCheckout (date): Data de saída.
            cliente (Cliente): Instância do cliente solicitante.
            quarto (Quarto): Instância do quarto a ser ocupado.
            idReserva (int, optional): ID manual, se fornecido (usado em persistência).
        
        Raises:
            ValueError: Se a data de checkout não for posterior à de checkin.
            Exception: Se o quarto selecionado não estiver disponível no momento.
        """
        # Validação lógica de Datas
        if not isinstance(dataCheckin, date) or not isinstance(dataCheckout, date):
            raise ValueError("As datas de check-in e check-out devem ser objetos do tipo date.")
            
        if dataCheckout <= dataCheckin:
            raise ValueError("Erro de Integridade: A data de check-out deve ser obrigatoriamente posterior à data de check-in.")
        
        # Validação de disponibilidade do Quarto (Estado do objeto composto)
        if not quarto.disponivel:
            raise Exception(f"Operação Inválida: O Quarto {quarto.numero} já se encontra ocupado ou em manutenção.")
        
        # Gerenciamento de Identificador Único
        if idReserva is None:
            Reserva._contador_id += 1
            self._idReserva = Reserva._contador_id
        else:
            self._idReserva = idReserva
            if idReserva > Reserva._contador_id:
                Reserva._contador_id = idReserva
        
        # Atributos protegidos (Encapsulamento)
        self._dataCheckin = dataCheckin
        self._dataCheckout = dataCheckout
        self._valorTotal = 0.0  # Inicializado em zero, calculado externamente pelo FinanceiroService
        self._cliente = cliente
        self._quarto = quarto
        
        # Alteração de estado do objeto associado (Composição)
        # O Quarto passa a ser ocupado no momento da confirmação da reserva
        quarto.marcarOcupado()

    # --- PROPRIEDADES (GETTERS E SETTERS) COM VALIDAÇÕES ---

    @property
    def idReserva(self) -> int:
        """Retorna o identificador único da reserva."""
        return self._idReserva

    @property
    def dataCheckin(self) -> date:
        """Retorna a data de check-in da reserva."""
        return self._dataCheckin
    
    @dataCheckin.setter
    def dataCheckin(self, valor: date):
        """Define a data de check-in com validação de consistência."""
        if not isinstance(valor, date):
            raise ValueError("Tipo Inválido: A data deve ser uma instância de datetime.date.")
        if hasattr(self, '_dataCheckout') and valor >= self._dataCheckout:
            raise ValueError("Consistência de Datas: O Check-in não pode ocorrer após ou no mesmo dia do Check-out.")
        self._dataCheckin = valor

    @property
    def dataCheckout(self) -> date:
        """Retorna a data de check-out da reserva."""
        return self._dataCheckout
    
    @dataCheckout.setter
    def dataCheckout(self, valor: date):
        """Define a data de check-out com validação de consistência."""
        if not isinstance(valor, date):
            raise ValueError("Tipo Inválido: A data deve ser uma instância de datetime.date.")
        if hasattr(self, '_dataCheckin') and valor <= self._dataCheckin:
            raise ValueError("Consistência de Datas: O Check-out deve ser estritamente posterior ao Check-in.")
        self._dataCheckout = valor

    @property
    def valorTotal(self) -> float:
        """Retorna o valor total da reserva calculado pelo FinanceiroService."""
        return self._valorTotal
    
    @valorTotal.setter
    def valorTotal(self, valor: float):
        """
        Define o valor total da reserva.
        Aplica SRP: Este valor deve ser calculado por FinanceiroService e injetado aqui.
        """
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("Erro Financeiro: O valor total da fatura não pode ser negativo.")
        self._valorTotal = float(valor)

    @property
    def cliente(self) -> 'Cliente':
        """Retorna a instância do Cliente associado à esta reserva."""
        return self._cliente
    
    @property
    def quarto(self) -> 'Quarto':
        """Retorna a instância do Quarto associado à esta reserva."""
        return self._quarto

    # --- MÉTODOS DE COMPORTAMENTO ---

    def confirmarReserva(self) -> bool:
        """
        Realiza a confirmação formal da reserva no sistema.
        
        Returns:
            bool: True se a confirmação foi processada com sucesso.
        """
        print(f"[LOG] Sistema: Reserva #{self.idReserva} confirmada para o cliente {self.cliente.nome}.")
        return True
    
    def cancelarReserva(self) -> bool:
        """
        Cancela a reserva atual e restaura a disponibilidade do quarto associado.
        Aplica lógica de alteração de estado entre objetos relacionados.
        
        Returns:
            bool: True se o cancelamento e a liberação do quarto foram concluídos.
        """
        print(f"[LOG] Sistema: Processando cancelamento da reserva #{self.idReserva}...")
        self.quarto.liberarQuarto()
        print(f"[LOG] Sistema: Quarto {self.quarto.numero} liberado e disponível para novas reservas.")
        return True
    
    def __str__(self):
        """
        Retorna uma representação textual detalhada do objeto Reserva.
        Utilizado para exibição em logs e listagens da interface.
        """
        return (f"Reserva ID: {self.idReserva} | "
                f"Hóspede: {self.cliente.nome} | "
                f"Acomodação: Quarto {self.quarto.numero} ({self.quarto.tipo}) | "
                f"Período: {self.dataCheckin.strftime('%d/%m/%Y')} até {self.dataCheckout.strftime('%d/%m/%Y')} | "
                f"Status Financeiro: R$ {self.valorTotal:.2f}")