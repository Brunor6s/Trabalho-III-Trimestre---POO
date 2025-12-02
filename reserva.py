"""
Módulo reserva - Define a classe Reserva.
"""

from datetime import date
from typing import TYPE_CHECKING

# Evita importação circular
if TYPE_CHECKING:
    from .cliente import Cliente
    from .quarto import Quarto


class Reserva:
    """
    Classe que representa uma reserva de quarto no hotel.
    
    Demonstra composição: uma Reserva possui um Cliente e um Quarto.
    
    Atributos:
        idReserva (int): Identificador único da reserva
        dataCheckin (date): Data de check-in
        dataCheckout (date): Data de check-out
        valorTotal (float): Valor total da reserva
        cliente (Cliente): Cliente que fez a reserva
        quarto (Quarto): Quarto reservado
    """
    
    _contador_id = 0
    
    def __init__(self, dataCheckin: date, dataCheckout: date, cliente: 'Cliente', quarto: 'Quarto', idReserva: int = None):
        """
        Inicializa uma reserva.
        
        Args:
            dataCheckin (date): Data de entrada
            dataCheckout (date): Data de saída
            cliente (Cliente): Cliente da reserva
            quarto (Quarto): Quarto reservado
            idReserva (int, optional): ID da reserva. Se None, será gerado automaticamente.
        
        Raises:
            ValueError: Se as datas forem inválidas
            Exception: Se o quarto não estiver disponível
        """
        # Validação de datas
        if dataCheckout <= dataCheckin:
            raise ValueError("Data de check-out deve ser posterior à data de check-in.")
        
        # Validação de disponibilidade do quarto
        if not quarto.disponivel:
            raise Exception("Quarto não está disponível.")
        
        # Gera ID se não fornecido
        if idReserva is None:
            Reserva._contador_id += 1
            self._idReserva = Reserva._contador_id
        else:
            self._idReserva = idReserva
            if idReserva > Reserva._contador_id:
                Reserva._contador_id = idReserva
        
        self._dataCheckin = dataCheckin
        self._dataCheckout = dataCheckout
        self._valorTotal = 0.0
        self._cliente = cliente
        self._quarto = quarto
        
        # Marca o quarto como ocupado
        quarto.marcarOcupado()
        
        # Calcula o valor total automaticamente
        self.calcularTotal()
    
    @property
    def idReserva(self) -> int:
        """Retorna o ID da reserva."""
        return self._idReserva
    
    @property
    def dataCheckin(self) -> date:
        """Retorna a data de check-in."""
        return self._dataCheckin
    
    @dataCheckin.setter
    def dataCheckin(self, valor: date):
        """
        Define a data de check-in.
        
        Args:
            valor (date): Nova data de check-in
        
        Raises:
            ValueError: Se a data for inválida
        """
        if not isinstance(valor, date):
            raise ValueError("Data de check-in deve ser do tipo date.")
        
        if hasattr(self, '_dataCheckout') and self._dataCheckout and valor >= self._dataCheckout:
            raise ValueError("Data de check-in deve ser anterior à data de check-out.")
        
        self._dataCheckin = valor
    
    @property
    def dataCheckout(self) -> date:
        """Retorna a data de check-out."""
        return self._dataCheckout
    
    @dataCheckout.setter
    def dataCheckout(self, valor: date):
        """
        Define a data de check-out.
        
        Args:
            valor (date): Nova data de check-out
        
        Raises:
            ValueError: Se a data for inválida
        """
        if not isinstance(valor, date):
            raise ValueError("Data de check-out deve ser do tipo date.")
        
        if hasattr(self, '_dataCheckin') and self._dataCheckin and valor <= self._dataCheckin:
            raise ValueError("Data de check-out deve ser posterior à data de check-in.")
        
        self._dataCheckout = valor
    
    @property
    def valorTotal(self) -> float:
        """Retorna o valor total da reserva."""
        return self._valorTotal
    
    @property
    def cliente(self) -> 'Cliente':
        """Retorna o cliente da reserva."""
        return self._cliente
    
    @property
    def quarto(self) -> 'Quarto':
        """Retorna o quarto da reserva."""
        return self._quarto
    
    def calcularTotal(self) -> float:
        """
        Calcula o valor total da reserva baseado nas datas e no preço da diária.
        
        Returns:
            float: Valor total da reserva
        """
        dias = (self.dataCheckout - self.dataCheckin).days
        self._valorTotal = dias * self.quarto.precoDiaria
        return self._valorTotal
    
    def confirmarReserva(self) -> bool:
        """
        Confirma a reserva.
        
        Returns:
            bool: True se confirmada com sucesso
        """
        print(f"Reserva {self.idReserva} confirmada para {self.cliente.nome}.")
        return True
    
    def cancelarReserva(self) -> bool:
        """
        Cancela a reserva e libera o quarto.
        
        Returns:
            bool: True se cancelada com sucesso
        """
        print(f"Reserva {self.idReserva} cancelada.")
        self.quarto.liberarQuarto()
        return True
    
    def __str__(self):
        """Retorna representação em string da reserva."""
        return (f"Reserva {self.idReserva} - Cliente: {self.cliente.nome} - "
                f"Quarto: {self.quarto.numero} - {self.dataCheckin} -> {self.dataCheckout} - "
                f"Total: R$ {self.valorTotal:.2f}")
