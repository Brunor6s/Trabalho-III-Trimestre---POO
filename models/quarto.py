"""
Módulo quarto - Define a classe Quarto e suas especializações.
Aplicando OCP (Open-Closed) e LSP (Liskov Substitution).
"""
from abc import ABC, abstractmethod

class Quarto(ABC):
    """
    Classe abstrata que representa um quarto do hotel.
    
    Atributos:
        numero (int): Número do quarto
        disponivel (bool): Status de disponibilidade do quarto
    """
    
    def __init__(self, numero: int):
        """
        Inicializa um quarto base.
        
        Args:
            numero (int): Número do quarto
        """
        self._numero = None
        self._disponivel = True
        
        # Usa property para validação original
        self.numero = numero
    
    @property
    def numero(self) -> int:
        """Retorna o número do quarto."""
        return self._numero
    
    @numero.setter
    def numero(self, valor: int):
        """
        Define o número do quarto com validação estrita.
        """
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Número do quarto deve ser um inteiro positivo.")
        self._numero = valor
    
    @property
    @abstractmethod
    def precoDiaria(self) -> float:
        """Método abstrato: Cada subclasse define seu preço (OCP)."""
        pass

    @property
    @abstractmethod
    def tipo(self) -> str:
        """Método abstrato: Cada subclasse define seu tipo string (OCP)."""
        pass

    @property
    def disponivel(self) -> bool:
        """Retorna se o quarto está disponível."""
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, valor: bool):
        """Define a disponibilidade do quarto."""
        self._disponivel = bool(valor)
    
    def marcarOcupado(self):
        """Marca o quarto como ocupado."""
        self._disponivel = False
    
    def liberarQuarto(self):
        """Libera o quarto, marcando-o como disponível."""
        self._disponivel = True
    
    def revisarAposCheckout(self):
        """Registra necessidade de revisão."""
        print(f"Quarto {self.numero} precisa ser revisado após checkout.")
        return True
    
    def __str__(self):
        """Representação em string respeitando o polimorfismo."""
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} - {self.tipo} - R$ {self.precoDiaria:.2f} - {status}"

# --- SUBCLASSES QUE EXTENDEM O QUARTO (OCP EM AÇÃO) ---

class QuartoSolteiro(Quarto):
    @property
    def precoDiaria(self): return 150.0
    @property
    def tipo(self): return "Solteiro"

class QuartoCasal(Quarto):
    @property
    def precoDiaria(self): return 200.0
    @property
    def tipo(self): return "Casal"

class QuartoLuxo(Quarto):
    @property
    def precoDiaria(self): return 350.0
    @property
    def tipo(self): return "Luxo"

class QuartoPresidencial(Quarto):
    @property
    def precoDiaria(self): return 1000.0
    @property
    def tipo(self): return "Presidencial"