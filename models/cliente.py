"""
Módulo cliente - Define a classe Cliente.
"""

import re
from .pessoa import Pessoa


class Cliente(Pessoa):
    """
    Classe que representa um cliente do hotel.
    
    Herda de Pessoa e adiciona atributos específicos de cliente.
    
    Atributos:
        idCliente (int): Identificador único do cliente
        telefone (str): Telefone de contato do cliente
        senha (str): Senha para login no sistema
    """
    
    _contador_id = 0
    
    def __init__(self, nome: str, documento: str, email: str, telefone: str, senha: str, idCliente: int = None):
        """
        Inicializa um cliente.
        
        Args:
            nome (str): Nome completo do cliente
            documento (str): CPF do cliente
            email (str): Email do cliente
            telefone (str): Telefone do cliente
            senha (str): Senha para login
            idCliente (int, optional): ID do cliente. Se None, será gerado automaticamente.
        
        Raises:
            ValueError: Se algum parâmetro for inválido
        """
        super().__init__(nome, documento, email)
        
        self._idCliente = None
        self._telefone = None
        self._senha = None
        
        # Gera ID se não fornecido
        if idCliente is None:
            Cliente._contador_id += 1
            self._idCliente = Cliente._contador_id
        else:
            self.idCliente = idCliente
        
        # Usa properties para validação
        self.telefone = telefone
        self.senha = senha
    
    @property
    def idCliente(self) -> int:
        """Retorna o ID do cliente."""
        return self._idCliente
    
    @idCliente.setter
    def idCliente(self, valor: int):
        """
        Define o ID do cliente.
        
        Args:
            valor (int): ID do cliente
        
        Raises:
            ValueError: Se o ID for inválido
        """
        if valor is None or valor <= 0:
            raise ValueError("ID do cliente deve ser um número positivo.")
        self._idCliente = valor
        
        # Atualiza contador se necessário
        if valor > Cliente._contador_id:
            Cliente._contador_id = valor
    
    @property
    def telefone(self) -> str:
        """Retorna o telefone do cliente."""
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor: str):
        """
        Define o telefone do cliente.
        
        Args:
            valor (str): Telefone do cliente
        
        Raises:
            ValueError: Se o telefone for inválido
        """
        if not valor:
            raise ValueError("Telefone é obrigatório.")
        
        tel_clean = valor.strip()
        
        # Permitir dígitos, espaços, parênteses e traço
        if not re.match(r"^[0-9\s\(\)\-]+$", tel_clean):
            raise ValueError("Telefone inválido: use apenas dígitos, espaços, parênteses e '-'")
        
        # Verifica se tem ao menos 8 dígitos
        digits = re.sub(r"\D", "", tel_clean)
        if len(digits) < 8:
            raise ValueError("Telefone inválido: deve ter no mínimo 8 dígitos.")
        
        self._telefone = tel_clean
    
    @property
    def senha(self) -> str:
        """Retorna a senha do cliente."""
        return self._senha
    
    @senha.setter
    def senha(self, valor: str):
        """
        Define a senha do cliente.
        
        Args:
            valor (str): Senha do cliente
        
        Raises:
            ValueError: Se a senha for inválida
        """
        if not valor or len(valor.strip()) < 3:
            raise ValueError("Senha deve ter no mínimo 3 caracteres.")
        
        self._senha = valor
    
    def exibirDados(self):
        """Exibe os dados do cliente no console."""
        print("Cliente:")
        print("ID:", self.idCliente)
        print("Nome:", self.nome)
        print("Documento:", self.documento)
        print("Email:", self.email)
        print("Telefone:", self.telefone)
    
    def solicitarReserva(self):
        """Método para solicitar uma reserva (placeholder)."""
        print(f"Cliente {self.nome} está solicitando uma reserva...")
    
    def __str__(self):
        """Retorna representação em string do cliente."""
        return f"Cliente {self.idCliente} - {self.nome} | {self.documento} | {self.email} | {self.telefone}"
