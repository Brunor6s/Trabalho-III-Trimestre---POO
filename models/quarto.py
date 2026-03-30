"""
Módulo quarto - Define a hierarquia de quartos do hotel seguindo SOLID.

Princípios Aplicados:
- OCP (Open-Closed Principle): A classe base Quarto está fechada para modificação, 
  mas aberta para novos tipos de acomodação via herança.
- LSP (Liskov Substitution Principle): Subclasses de Quarto podem substituir 
  a classe base sem quebrar a lógica de disponibilidade e identificação.
"""
from abc import ABC, abstractmethod

class Quarto(ABC):
    """
    Classe abstrata que representa a estrutura base de um quarto.
    Encapsula o estado de disponibilidade e a identificação numérica.
    """
    
    def __init__(self, numero: int):
        """
        Inicializa os atributos protegidos do quarto.
        
        Args:
            numero (int): Identificador numérico único do quarto.
        """
        self._numero = None
        self._disponivel = True
        
        # Atribuição via setter para disparar validações
        self.numero = numero
    
    @property
    def numero(self) -> int:
        """Retorna o identificador numérico do quarto."""
        return self._numero
    
    @numero.setter
    def numero(self, valor: int):
        """
        Valida e define o número do quarto.
        
        Raises:
            ValueError: Se o número fornecido não for um inteiro positivo.
        """
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Erro de Cadastro: O número do quarto deve ser um valor inteiro estritamente positivo.")
        self._numero = valor
    
    @property
    @abstractmethod
    def precoDiaria(self) -> float:
        """
        Método abstrato que obriga subclasses a definirem seu preço.
        Aplica OCP: Novos preços são definidos em novas classes, não em ifs.
        """
        pass

    @property
    @abstractmethod
    def tipo(self) -> str:
        """Retorna o nome do tipo do quarto em formato string."""
        pass

    @property
    def disponivel(self) -> bool:
        """Retorna o status atual de ocupação do quarto."""
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, valor: bool):
        """Define explicitamente a disponibilidade (True=Livre, False=Ocupado)."""
        self._disponivel = bool(valor)
    
    def marcarOcupado(self):
        """Altera o estado do quarto para indisponível."""
        self._disponivel = False
    
    def liberarQuarto(self):
        """Restaura a disponibilidade do quarto para novas reservas."""
        self._disponivel = True
    
    def revisarAposCheckout(self) -> bool:
        """
        Simula o processo de revisão e limpeza obrigatória.
        
        Returns:
            bool: Status da operação de revisão.
        """
        print(f"[REVISÃO] Quarto {self.numero} entrou em fila de limpeza.")
        return True
    
    def __str__(self):
        """Representação textual rica para listagem em tabelas e logs."""
        status = "✅ DISPONÍVEL" if self.disponivel else "❌ OCUPADO"
        return (f"Acomodação {self.numero:03d} | "
                f"Categoria: {self.tipo:12s} | "
                f"Diária: R$ {self.precoDiaria:8.2f} | "
                f"Status: {status}")

# --- SUBCLASSES ESPECIALIZADAS (OCP / LSP) ---

class QuartoSolteiro(Quarto):
    """Especialização para hóspedes individuais."""
    @property
    def precoDiaria(self) -> float: return 150.0
    @property
    def tipo(self) -> str: return "Solteiro"

class QuartoCasal(Quarto):
    """Especialização para casais ou duplas."""
    @property
    def precoDiaria(self) -> float: return 220.0
    @property
    def tipo(self) -> str: return "Casal"

class QuartoLuxo(Quarto):
    """Especialização de alto padrão com serviços adicionais."""
    @property
    def precoDiaria(self) -> float: return 450.0
    @property
    def tipo(self) -> str: return "Luxo"

class QuartoPresidencial(Quarto):
    """Categoria máxima do hotel com infraestrutura completa."""
    @property
    def precoDiaria(self) -> float: return 1250.0
    @property
    def tipo(self) -> str: return "Presidencial"