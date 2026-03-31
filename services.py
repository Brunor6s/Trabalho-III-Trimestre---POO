"""
Módulo services - Gerencia as operações de negócio do sistema de hotel.

Este módulo foi refatorado para seguir os princípios SOLID:
- SRP: Lógica financeira movida para FinanceiroService.
- DIP: Serviços recebem repositórios (listas) via construtor.
"""

from models import Cliente, Funcionario, Quarto, Reserva
from datetime import date


class FinanceiroService:
    """
    Novo Serviço (Princípio SRP): Responsável exclusivamente por cálculos financeiros.
    Anteriormente, essa lógica estava espalhada entre Reserva e ReservaService.
    """
    
    def calcular_fatura(self, reserva: Reserva) -> float:
        """
        Calcula o valor total de uma reserva.
        
        Args:
            reserva (Reserva): O objeto da reserva.
            
        Returns:
            float: O valor total calculado.
        """
        dias = (reserva.dataCheckout - reserva.dataCheckin).days
        if dias <= 0:
            dias = 1
            
        # O preço da diária é obtido via polimorfismo (Princípio LSP)
        total = dias * reserva.quarto.precoDiaria
        reserva.valorTotal = total
        return total


class CalculadoraPreco:
    def calcular(self, quarto):
        if quarto.tipo == "simples":
            return 100
        elif quarto.tipo == "luxo":
            return 200
        elif quarto.tipo == "suite":
            return 300


class ClienteService:
    """
    Serviço para gerenciamento de clientes.
    Aplica DIP: Recebe a lista de persistência por injeção de dependência.
    """
    
    def __init__(self, repositorio_clientes: list):
        """
        Inicializa o serviço de clientes.
        
        Args:
            repositorio_clientes (list): Lista onde os clientes são armazenados.
        """
        self._clientes = repositorio_clientes
    
    @property
    def clientes(self):
        """Retorna a lista de clientes cadastrados."""
        return self._clientes
    
    def criar(self, nome: str, documento: str, email: str, senha: str, telefone: str = "00000-0000", autor: str = "dono") -> Cliente:
        """
        Cria e cadastra um novo cliente com validações estritas.
        """
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem cadastrar clientes.")
        
        for c in self._clientes:
            if c.documento == documento.strip():
                raise ValueError("Já existe cliente com este documento (CPF).")
        
        novo_cliente = Cliente(nome=nome, documento=documento, email=email, 
                              telefone=telefone, senha=senha)
        
        self._clientes.append(novo_cliente)
        return novo_cliente
    
    def cadastrarCliente(self, cliente: Cliente, autor: str = "dono") -> str:
        """Cadastra um cliente já instanciado."""
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem cadastrar clientes.")
        
        for c in self._clientes:
            if c.documento == cliente.documento:
                raise ValueError("Já existe cliente com este documento (CPF).")
        
        self._clientes.append(cliente)
        return "Cliente cadastrado com sucesso!"
    
    def listarClientes(self):
        """Retorna a lista completa de clientes."""
        return self._clientes
    
    def buscarPorEmail(self, email: str) -> Cliente:
        """Busca um cliente pelo email."""
        for cliente in self._clientes:
            if cliente.email == email:
                return cliente
        return None
    
    def buscarPorId(self, id_cliente: int) -> Cliente:
        """Busca um cliente pelo ID único."""
        for cliente in self._clientes:
            if cliente.idCliente == id_cliente:
                return cliente
        return None
    
    def editar(self, id_cliente: int, nome: str = None, email: str = None, 
              telefone: str = None, senha: str = None, autor: str = "dono") -> Cliente:
        """Edita dados de um cliente existente com validação de autor."""
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem editar clientes.")
        
        cliente = self.buscarPorId(id_cliente)
        if not cliente:
            raise ValueError("Cliente não encontrado.")
        
        if nome: cliente.nome = nome
        if email: cliente.email = email
        if telefone: cliente.telefone = telefone
        if senha: cliente.senha = senha
        
        return cliente
    
    def excluir(self, id_cliente: int, autor: str = "dono") -> str:
        """Remove um cliente do sistema."""
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem excluir clientes.")
        
        cliente = self.buscarPorId(id_cliente)
        if not cliente:
            raise ValueError("Cliente não encontrado.")
        
        self._clientes.remove(cliente)
        return f"Cliente {cliente.nome} excluído com sucesso!"


class FuncionarioService:
    """
    Serviço para gerenciamento de funcionários.
    Aplica DIP e SRP.
    """
    
    def __init__(self, repositorio_funcionarios: list):
        self._funcionarios = repositorio_funcionarios
    
    @property
    def funcionarios(self):
        return self._funcionarios
    
    def criar(self, nome: str, email: str, senha: str, documento: str = "00000000000", 
             cargo: str = "Recepcionista", autor: str = "dono") -> Funcionario:
        """Cria um novo funcionário. Somente o Dono tem permissão (SRP/Segurança)."""
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar funcionários.")
        
        for f in self._funcionarios:
            if f.documento == documento.strip():
                raise ValueError("Já existe funcionário com este documento.")
        
        novo_funcionario = Funcionario(nome=nome, documento=documento, email=email,
                                      cargo=cargo, senha=senha)
        
        self._funcionarios.append(novo_funcionario)
        return novo_funcionario

    def cadastrarFuncionario(self, funcionario: Funcionario, autor: str = "dono") -> str:
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar funcionários.")
        self._funcionarios.append(funcionario)
        return "Funcionário cadastrado com sucesso!"

    def listarFuncionarios(self):
        return self._funcionarios
    
    def buscarPorEmail(self, email: str) -> Funcionario:
        for funcionario in self._funcionarios:
            if funcionario.email == email:
                return funcionario
        return None
    
    def buscarPorId(self, id_funcionario: int) -> Funcionario:
        for funcionario in self._funcionarios:
            if funcionario.idFuncionario == id_funcionario:
                return funcionario
        return None
    
    def editar(self, id_funcionario: int, nome: str = None, email: str = None,
              cargo: str = None, senha: str = None, autor: str = "dono") -> Funcionario:
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode editar funcionários.")
        
        funcionario = self.buscarPorId(id_funcionario)
        if not funcionario:
            raise ValueError("Funcionário não encontrado.")
        
        if nome: funcionario.nome = nome
        if email: funcionario.email = email
        if cargo: funcionario.cargo = cargo
        if senha: funcionario.senha = senha
        
        return funcionario
    
    def excluir(self, id_funcionario: int, autor: str = "dono") -> str:
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode excluir funcionários.")
        funcionario = self.buscarPorId(id_funcionario)
        if not funcionario:
            raise ValueError("Funcionário não encontrado.")
        self._funcionarios.remove(funcionario)
        return f"Funcionário {funcionario.nome} excluído."


class QuartoService:
    """
    Serviço para gerenciamento de quartos.
    Adaptado para lidar com as novas subclasses polimórficas (OCP/LSP).
    """
    
    def __init__(self, repositorio_quartos: list):
        self._quartos = repositorio_quartos
    
    @property
    def quartos(self):
        return self._quartos
    
    def cadastrarQuarto(self, quarto: Quarto) -> str:
        """Cadastra um objeto Quarto (pode ser Simples, Luxo, etc)."""
        for q in self._quartos:
            if q.numero == quarto.numero:
                raise ValueError(f"Já existe quarto com o número {quarto.numero}.")
        self._quartos.append(quarto)
        return "Quarto cadastrado com sucesso!"
    
    def adicionarQuarto(self, quarto: Quarto) -> str:
        return self.cadastrarQuarto(quarto)
    
    def listarQuartos(self):
        return self._quartos
    
    def buscarDisponivel(self) -> Quarto:
        for quarto in self._quartos:
            if quarto.disponivel:
                return quarto
        return None
    
    def listarDisponiveis(self):
        return [q for q in self._quartos if q.disponivel]


class ReservaService:
    """
    Serviço para gerenciamento de reservas.
    Aplica DIP ao receber o repositório de reservas.
    Delegou o cálculo financeiro para o FinanceiroService (SRP).
    """
    
    def __init__(self, repositorio_reservas: list, financeiro_service):
        self._reservas = repositorio_reservas
        self._financeiro = financeiro_service
    
    @property
    def reservas(self):
        return self._reservas
    
    def criarReserva(self, dataEntrada: date, dataSaida: date, 
                 cliente: Cliente, quarto: Quarto, idReserva: int = None) -> Reserva:
        """Cria uma nova reserva."""
        multa = 0.5 if quarto.tipo == "luxo" else 0.0  # regra externa simples
        reserva = Reserva(dataCheckin=dataEntrada, dataCheckout=dataSaida, 
                         cliente=cliente, quarto=quarto, multa=multa, idReserva=idReserva)
        # Calcular o valor total da reserva
        self._financeiro.calcular_fatura(reserva)
        
        self._reservas.append(reserva)
        return reserva
    
    def cancelar(self, reserva: Reserva) -> str:
        """Cancela reserva e libera o quarto."""
        if reserva in self._reservas:
            reserva.cancelarReserva()
            self._reservas.remove(reserva)
            return "Reserva cancelada com sucesso!"
        return "Reserva não encontrada."
    
    def buscarPorCliente(self, cliente: Cliente):
        return [r for r in self._reservas if r.cliente == cliente]
    
    def buscarPorId(self, id_reserva: int):
        for reserva in self._reservas:
            if reserva.idReserva == id_reserva:
                return reserva
        return None