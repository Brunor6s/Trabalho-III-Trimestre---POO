"""
Módulo pessoa - Define a classe abstrata Pessoa.
"""

from abc import ABC, abstractmethod
import re


class Pessoa(ABC):
    """
    Classe abstrata que representa uma pessoa no sistema.
    
    Atributos:
        nome (str): Nome completo da pessoa
        documento (str): CPF da pessoa (apenas números)
        email (str): Email da pessoa
    """
    
    def __init__(self, nome: str, documento: str, email: str):
        """
        Inicializa uma pessoa.
        
        Args:
            nome (str): Nome completo da pessoa
            documento (str): CPF da pessoa
            email (str): Email da pessoa
        
        Raises:
            ValueError: Se algum parâmetro for inválido
        """
        self._nome = None
        self._documento = None
        self._email = None
        
        # Usa properties para validação
        self.nome = nome
        self.documento = documento
        self.email = email
    
    @property
    def nome(self) -> str:
        """Retorna o nome da pessoa."""
        return self._nome
    
    @nome.setter
    def nome(self, valor: str):
        """
        Define o nome da pessoa.
        
        Args:
            valor (str): Nome da pessoa
        
        Raises:
            ValueError: Se o nome for vazio ou inválido
        """
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor.strip()
    
    @property
    def documento(self) -> str:
        """Retorna o CPF da pessoa."""
        return self._documento
    
    @documento.setter
    def documento(self, valor: str):
        """
        Define o documento (CPF) da pessoa.
        
        Args:
            valor (str): CPF (pode conter formatação)
        
        Raises:
            ValueError: Se o CPF for inválido
        """
        if not valor:
            raise ValueError("Documento (CPF) é obrigatório.")
        
        # Remove caracteres não numéricos
        doc_clean = re.sub(r"\D", "", valor)
        
        # Valida: deve ter exatamente 11 dígitos
        if len(doc_clean) != 11:
            raise ValueError("Documento (CPF) inválido: deve ter exatamente 11 dígitos numéricos.")
        
        # Verifica se contém apenas números
        if not doc_clean.isdigit():
            raise ValueError("Documento (CPF) inválido: deve conter apenas números.")
        
        self._documento = doc_clean
    
    @property
    def email(self) -> str:
        """Retorna o email da pessoa."""
        return self._email
    
    @email.setter
    def email(self, valor: str):
        """
        Define o email da pessoa.
        
        Args:
            valor (str): Email da pessoa
        
        Raises:
            ValueError: Se o email for inválido
        """
        if not valor or "@" not in valor:
            raise ValueError("Email inválido.")
        
        # Validação simples: algo@algo.dom
        if not re.match(r"[^@]+@[^@]+\.[^@]+", valor):
            raise ValueError("Email inválido.")
        
        self._email = valor.strip()
    
    @abstractmethod
    def exibirDados(self):
        """Método abstrato para exibir dados da pessoa."""
        pass
    
    def __str__(self):
        """Retorna representação em string da pessoa."""
        return f"{self.nome} - {self.documento} - {self.email}"
