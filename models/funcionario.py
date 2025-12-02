"""
Módulo funcionario - Define a classe Funcionario.
"""

from .pessoa import Pessoa


class Funcionario(Pessoa):
    """
    Classe que representa um funcionário do hotel.
    
    Herda de Pessoa e adiciona atributos específicos de funcionário.
    
    Atributos:
        idFuncionario (int): Identificador único do funcionário
        cargo (str): Cargo do funcionário no hotel
        senha (str): Senha para login no sistema
    """
    
    _contador_id = 0
    
    def __init__(self, nome: str, documento: str, email: str, cargo: str, senha: str, idFuncionario: int = None):
        """
        Inicializa um funcionário.
        
        Args:
            nome (str): Nome completo do funcionário
            documento (str): CPF do funcionário
            email (str): Email do funcionário
            cargo (str): Cargo do funcionário
            senha (str): Senha para login
            idFuncionario (int, optional): ID do funcionário. Se None, será gerado automaticamente.
        
        Raises:
            ValueError: Se algum parâmetro for inválido
        """
        super().__init__(nome, documento, email)
        
        self._idFuncionario = None
        self._cargo = None
        self._senha = None
        
        # Gera ID se não fornecido
        if idFuncionario is None:
            Funcionario._contador_id += 1
            self._idFuncionario = Funcionario._contador_id
        else:
            self.idFuncionario = idFuncionario
        
        # Usa properties para validação
        self.cargo = cargo
        self.senha = senha
    
    @property
    def idFuncionario(self) -> int:
        """Retorna o ID do funcionário."""
        return self._idFuncionario
    
    @idFuncionario.setter
    def idFuncionario(self, valor: int):
        """
        Define o ID do funcionário.
        
        Args:
            valor (int): ID do funcionário
        
        Raises:
            ValueError: Se o ID for inválido
        """
        if valor is None or valor <= 0:
            raise ValueError("ID do funcionário deve ser um número positivo.")
        self._idFuncionario = valor
        
        # Atualiza contador se necessário
        if valor > Funcionario._contador_id:
            Funcionario._contador_id = valor
    
    @property
    def cargo(self) -> str:
        """Retorna o cargo do funcionário."""
        return self._cargo
    
    @cargo.setter
    def cargo(self, valor: str):
        """
        Define o cargo do funcionário.
        
        Args:
            valor (str): Cargo do funcionário
        
        Raises:
            ValueError: Se o cargo for inválido
        """
        if not valor or not valor.strip():
            raise ValueError("Cargo não pode ser vazio.")
        
        self._cargo = valor.strip()
    
    @property
    def senha(self) -> str:
        """Retorna a senha do funcionário."""
        return self._senha
    
    @senha.setter
    def senha(self, valor: str):
        """
        Define a senha do funcionário.
        
        Args:
            valor (str): Senha do funcionário
        
        Raises:
            ValueError: Se a senha for inválida
        """
        if not valor or len(valor.strip()) < 3:
            raise ValueError("Senha deve ter no mínimo 3 caracteres.")
        
        self._senha = valor
    
    def exibirDados(self):
        """Exibe os dados do funcionário no console."""
        print("Funcionário:")
        print("ID:", self.idFuncionario)
        print("Nome:", self.nome)
        print("Documento:", self.documento)
        print("Email:", self.email)
        print("Cargo:", self.cargo)
    
    def revisarQuarto(self, quarto=None):
        """
        Revisa um quarto após checkout.
        
        Args:
            quarto: Objeto Quarto a ser revisado (opcional)
        
        Returns:
            bool: True se a revisão foi bem-sucedida
        """
        if quarto:
            print(f"Funcionário {self.nome} revisou o quarto {quarto.numero}.")
        else:
            print(f"Funcionário {self.nome} realizou revisão de quarto.")
        return True
    
    def __str__(self):
        """Retorna representação em string do funcionário."""
        return f"Funcionario {self.idFuncionario} - {self.nome} | {self.cargo} | {self.documento} | {self.email}"
