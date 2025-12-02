"""
Módulo quarto - Define a classe Quarto.
"""


class Quarto:
    """
    Classe que representa um quarto do hotel.
    
    Atributos:
        numero (int): Número do quarto
        tipo (str): Tipo do quarto (Solteiro, Casal, Luxo, etc)
        precoDiaria (float): Preço da diária do quarto
        disponivel (bool): Status de disponibilidade do quarto
    """
    
    def __init__(self, numero: int, tipo: str, precoDiaria: float):
        """
        Inicializa um quarto.
        
        Args:
            numero (int): Número do quarto
            tipo (str): Tipo do quarto
            precoDiaria (float): Preço da diária
        
        Raises:
            ValueError: Se algum parâmetro for inválido
        """
        self._numero = None
        self._tipo = None
        self._precoDiaria = None
        self._disponivel = True
        
        # Usa properties para validação
        self.numero = numero
        self.tipo = tipo
        self.precoDiaria = precoDiaria
    
    @property
    def numero(self) -> int:
        """Retorna o número do quarto."""
        return self._numero
    
    @numero.setter
    def numero(self, valor: int):
        """
        Define o número do quarto.
        
        Args:
            valor (int): Número do quarto
        
        Raises:
            ValueError: Se o número for inválido
        """
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Número do quarto deve ser um inteiro positivo.")
        
        self._numero = valor
    
    @property
    def tipo(self) -> str:
        """Retorna o tipo do quarto."""
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor: str):
        """
        Define o tipo do quarto.
        
        Args:
            valor (str): Tipo do quarto
        
        Raises:
            ValueError: Se o tipo for inválido
        """
        if not valor or not valor.strip():
            raise ValueError("Tipo do quarto não pode ser vazio.")
        
        tipos_validos = ["Solteiro", "Casal", "Luxo", "Suite", "Presidencial"]
        valor_clean = valor.strip().capitalize()
        
        # Se não for um tipo padrão, aceita mesmo assim mas avisa
        if valor_clean not in tipos_validos:
            # Aceita qualquer tipo customizado
            pass
        
        self._tipo = valor.strip()
    
    @property
    def precoDiaria(self) -> float:
        """Retorna o preço da diária do quarto."""
        return self._precoDiaria
    
    @precoDiaria.setter
    def precoDiaria(self, valor: float):
        """
        Define o preço da diária do quarto.
        
        Args:
            valor (float): Preço da diária
        
        Raises:
            ValueError: Se o preço for inválido
        """
        try:
            valor_float = float(valor)
        except (ValueError, TypeError):
            raise ValueError("Preço da diária deve ser um número.")
        
        if valor_float <= 0:
            raise ValueError("Preço da diária deve ser positivo.")
        
        self._precoDiaria = valor_float
    
    @property
    def disponivel(self) -> bool:
        """Retorna se o quarto está disponível."""
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, valor: bool):
        """
        Define a disponibilidade do quarto.
        
        Args:
            valor (bool): True se disponível, False caso contrário
        """
        self._disponivel = bool(valor)
    
    def marcarOcupado(self):
        """Marca o quarto como ocupado."""
        self._disponivel = False
    
    def liberarQuarto(self):
        """Libera o quarto, marcando-o como disponível."""
        self._disponivel = True
    
    def revisarAposCheckout(self):
        """
        Marca que o quarto precisa ser revisado após checkout.
        
        Returns:
            bool: True indicando que a revisão foi registrada
        """
        print(f"Quarto {self.numero} precisa ser revisado após checkout.")
        return True
    
    def __str__(self):
        """Retorna representação em string do quarto."""
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} - {self.tipo} - R$ {self.precoDiaria:.2f} - {status}"
