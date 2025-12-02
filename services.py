"""
Módulo services - Gerencia as operações de negócio do sistema de hotel.

Este módulo contém os serviços responsáveis por gerenciar clientes, funcionários,
quartos e reservas, implementando a camada de lógica de negócios.
"""

from models import Cliente, Funcionario, Quarto, Reserva
from datetime import date


class ClienteService:
    """
    Serviço para gerenciamento de clientes.
    
    Responsável por criar, listar e gerenciar clientes do hotel.
    Implementa controle de permissões para cadastro.
    """
    
    def __init__(self):
        """Inicializa o serviço de clientes com lista vazia."""
        self._clientes = []
    
    @property
    def clientes(self):
        """Retorna a lista de clientes cadastrados."""
        return self._clientes
    
    def criar(self, nome: str, documento: str, email: str, senha: str, telefone: str = "00000-0000", autor: str = "dono") -> Cliente:
        """
        Cria e cadastra um novo cliente.
        
        Args:
            nome (str): Nome do cliente
            documento (str): CPF do cliente
            email (str): Email do cliente
            senha (str): Senha para login
            telefone (str, optional): Telefone do cliente
            autor (str, optional): Quem está cadastrando ('dono' ou 'funcionario')
        
        Returns:
            Cliente: Objeto cliente criado
        
        Raises:
            PermissionError: Se autor não tiver permissão
            ValueError: Se documento já estiver cadastrado ou dados inválidos
        """
        # Validação de permissão
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem cadastrar clientes.")
        
        # Verifica documento duplicado
        for c in self._clientes:
            if c.documento == documento.strip():
                raise ValueError("Já existe cliente com este documento (CPF).")
        
        # Cria o cliente (validações são feitas pelas properties)
        novo_cliente = Cliente(nome=nome, documento=documento, email=email, 
                              telefone=telefone, senha=senha)
        
        self._clientes.append(novo_cliente)
        return novo_cliente
    
    def cadastrarCliente(self, cliente: Cliente, autor: str = "dono") -> str:
        """
        Cadastra um cliente já criado.
        
        Args:
            cliente (Cliente): Objeto cliente a ser cadastrado
            autor (str, optional): Quem está cadastrando
        
        Returns:
            str: Mensagem de sucesso
        
        Raises:
            PermissionError: Se autor não tiver permissão
            ValueError: Se documento já estiver cadastrado
        """
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem cadastrar clientes.")
        
        # Verifica documento duplicado
        for c in self._clientes:
            if c.documento == cliente.documento:
                raise ValueError("Já existe cliente com este documento (CPF).")
        
        self._clientes.append(cliente)
        return "Cliente cadastrado com sucesso!"
    
    def listarClientes(self):
        """
        Lista todos os clientes cadastrados.
        
        Returns:
            list: Lista de clientes
        """
        return self._clientes
    
    def buscarPorEmail(self, email: str) -> Cliente:
        """
        Busca um cliente pelo email.
        
        Args:
            email (str): Email do cliente
        
        Returns:
            Cliente: Cliente encontrado ou None
        """
        for cliente in self._clientes:
            if cliente.email == email:
                return cliente
        return None
    
    def buscarPorId(self, id_cliente: int) -> Cliente:
        """
        Busca um cliente pelo ID.
        
        Args:
            id_cliente (int): ID do cliente
        
        Returns:
            Cliente: Cliente encontrado ou None
        """
        for cliente in self._clientes:
            if cliente.idCliente == id_cliente:
                return cliente
        return None
    
    def editar(self, id_cliente: int, nome: str = None, email: str = None, 
              telefone: str = None, senha: str = None, autor: str = "dono") -> Cliente:
        """
        Edita os dados de um cliente.
        
        Args:
            id_cliente (int): ID do cliente a editar
            nome (str, optional): Novo nome
            email (str, optional): Novo email
            telefone (str, optional): Novo telefone
            senha (str, optional): Nova senha
            autor (str): Quem está editando
        
        Returns:
            Cliente: Cliente editado
        
        Raises:
            PermissionError: Se autor não tiver permissão
            ValueError: Se cliente não for encontrado
        """
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem editar clientes.")
        
        cliente = self.buscarPorId(id_cliente)
        if not cliente:
            raise ValueError("Cliente não encontrado.")
        
        # Atualizar campos fornecidos
        if nome:
            cliente.nome = nome
        if email:
            cliente.email = email
        if telefone:
            cliente.telefone = telefone
        if senha:
            cliente.senha = senha
        
        return cliente
    
    def excluir(self, id_cliente: int, autor: str = "dono") -> str:
        """
        Exclui um cliente do sistema.
        
        Args:
            id_cliente (int): ID do cliente a excluir
            autor (str): Quem está excluindo
        
        Returns:
            str: Mensagem de sucesso
        
        Raises:
            PermissionError: Se autor não tiver permissão
            ValueError: Se cliente não for encontrado
        """
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
    
    Responsável por criar, listar e gerenciar funcionários do hotel.
    Apenas o dono pode cadastrar funcionários.
    """
    
    def __init__(self):
        """Inicializa o serviço de funcionários com lista vazia."""
        self._funcionarios = []
    
    @property
    def funcionarios(self):
        """Retorna a lista de funcionários cadastrados."""
        return self._funcionarios
    
    def criar(self, nome: str, email: str, senha: str, documento: str = "00000000000", 
             cargo: str = "Recepcionista", autor: str = "dono") -> Funcionario:
        """
        Cria e cadastra um novo funcionário.
        
        Args:
            nome (str): Nome do funcionário
            email (str): Email do funcionário
            senha (str): Senha para login
            documento (str, optional): CPF do funcionário
            cargo (str, optional): Cargo do funcionário
            autor (str, optional): Quem está cadastrando (deve ser 'dono')
        
        Returns:
            Funcionario: Objeto funcionário criado
        
        Raises:
            PermissionError: Se autor não for 'dono'
            ValueError: Se documento já estiver cadastrado ou dados inválidos
        """
        # Somente dono pode cadastrar funcionário
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar funcionários.")
        
        # Verifica documento duplicado
        for f in self._funcionarios:
            if f.documento == documento.strip():
                raise ValueError("Já existe funcionário com este documento (CPF).")
        
        # Cria o funcionário (validações são feitas pelas properties)
        novo_funcionario = Funcionario(nome=nome, documento=documento, email=email,
                                      cargo=cargo, senha=senha)
        
        self._funcionarios.append(novo_funcionario)
        return novo_funcionario
    
    def cadastrarFuncionario(self, funcionario: Funcionario, autor: str = "dono") -> str:
        """
        Cadastra um funcionário já criado.
        
        Args:
            funcionario (Funcionario): Objeto funcionário a ser cadastrado
            autor (str, optional): Quem está cadastrando (deve ser 'dono')
        
        Returns:
            str: Mensagem de sucesso
        
        Raises:
            PermissionError: Se autor não for 'dono'
            ValueError: Se documento já estiver cadastrado
        """
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar funcionários.")
        
        # Verifica documento duplicado
        for f in self._funcionarios:
            if f.documento == funcionario.documento:
                raise ValueError("Já existe funcionário com este documento (CPF).")
        
        self._funcionarios.append(funcionario)
        return "Funcionário cadastrado com sucesso!"
    
    def listarFuncionarios(self):
        """
        Lista todos os funcionários cadastrados.
        
        Returns:
            list: Lista de funcionários
        """
        return self._funcionarios
    
    def buscarPorEmail(self, email: str) -> Funcionario:
        """
        Busca um funcionário pelo email.
        
        Args:
            email (str): Email do funcionário
        
        Returns:
            Funcionario: Funcionário encontrado ou None
        """
        for funcionario in self._funcionarios:
            if funcionario.email == email:
                return funcionario
        return None
    
    def buscarPorId(self, id_funcionario: int) -> Funcionario:
        """
        Busca um funcionário pelo ID.
        
        Args:
            id_funcionario (int): ID do funcionário
        
        Returns:
            Funcionario: Funcionário encontrado ou None
        """
        for funcionario in self._funcionarios:
            if funcionario.idFuncionario == id_funcionario:
                return funcionario
        return None
    
    def editar(self, id_funcionario: int, nome: str = None, email: str = None,
              cargo: str = None, senha: str = None, autor: str = "dono") -> Funcionario:
        """
        Edita os dados de um funcionário.
        
        Args:
            id_funcionario (int): ID do funcionário a editar
            nome (str, optional): Novo nome
            email (str, optional): Novo email
            cargo (str, optional): Novo cargo
            senha (str, optional): Nova senha
            autor (str): Quem está editando
        
        Returns:
            Funcionario: Funcionário editado
        
        Raises:
            PermissionError: Se autor não for dono
            ValueError: Se funcionário não for encontrado
        """
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode editar funcionários.")
        
        funcionario = self.buscarPorId(id_funcionario)
        if not funcionario:
            raise ValueError("Funcionário não encontrado.")
        
        # Atualizar campos fornecidos
        if nome:
            funcionario.nome = nome
        if email:
            funcionario.email = email
        if cargo:
            funcionario.cargo = cargo
        if senha:
            funcionario.senha = senha
        
        return funcionario
    
    def excluir(self, id_funcionario: int, autor: str = "dono") -> str:
        """
        Exclui um funcionário do sistema.
        
        Args:
            id_funcionario (int): ID do funcionário a excluir
            autor (str): Quem está excluindo
        
        Returns:
            str: Mensagem de sucesso
        
        Raises:
            PermissionError: Se autor não for dono
            ValueError: Se funcionário não for encontrado
        """
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode excluir funcionários.")
        
        funcionario = self.buscarPorId(id_funcionario)
        if not funcionario:
            raise ValueError("Funcionário não encontrado.")
        
        self._funcionarios.remove(funcionario)
        return f"Funcionário {funcionario.nome} excluído com sucesso!"


class QuartoService:
    """
    Serviço para gerenciamento de quartos.
    
    Responsável por criar, listar e gerenciar quartos do hotel.
    """
    
    def __init__(self):
        """Inicializa o serviço de quartos com lista vazia."""
        self._quartos = []
    
    @property
    def quartos(self):
        """Retorna a lista de quartos cadastrados."""
        return self._quartos
    
    def criar(self, numero: str, preco: str, tipo: str = "Solteiro") -> Quarto:
        """
        Cria e cadastra um novo quarto.
        
        Args:
            numero (str): Número do quarto
            preco (str): Preço da diária
            tipo (str, optional): Tipo do quarto
        
        Returns:
            Quarto: Objeto quarto criado
        
        Raises:
            ValueError: Se número já estiver cadastrado ou dados inválidos
        """
        # Converte número para int
        try:
            numero_int = int(numero)
        except ValueError:
            raise ValueError("Número do quarto deve ser numérico.")
        
        # Verifica número duplicado
        for q in self._quartos:
            if q.numero == numero_int:
                raise ValueError(f"Já existe quarto com o número {numero_int}.")
        
        # Cria o quarto (validações são feitas pelas properties)
        novo_quarto = Quarto(numero=numero_int, tipo=tipo, precoDiaria=float(preco))
        
        self._quartos.append(novo_quarto)
        return novo_quarto
    
    def cadastrarQuarto(self, quarto: Quarto) -> str:
        """
        Cadastra um quarto já criado.
        
        Args:
            quarto (Quarto): Objeto quarto a ser cadastrado
        
        Returns:
            str: Mensagem de sucesso
        
        Raises:
            ValueError: Se número já estiver cadastrado
        """
        # Verifica número duplicado
        for q in self._quartos:
            if q.numero == quarto.numero:
                raise ValueError(f"Já existe quarto com o número {quarto.numero}.")
        
        self._quartos.append(quarto)
        return "Quarto cadastrado com sucesso!"
    
    def adicionarQuarto(self, quarto: Quarto) -> str:
        """
        Adiciona um quarto (alias para cadastrarQuarto).
        
        Args:
            quarto (Quarto): Objeto quarto a ser adicionado
        
        Returns:
            str: Mensagem de sucesso
        """
        return self.cadastrarQuarto(quarto)
    
    def listarQuartos(self):
        """
        Lista todos os quartos cadastrados.
        
        Returns:
            list: Lista de quartos
        """
        return self._quartos
    
    def buscarDisponivel(self) -> Quarto:
        """
        Busca o primeiro quarto disponível.
        
        Returns:
            Quarto: Primeiro quarto disponível ou None
        """
        for quarto in self._quartos:
            if quarto.disponivel:
                return quarto
        return None
    
    def listarDisponiveis(self):
        """
        Lista todos os quartos disponíveis.
        
        Returns:
            list: Lista de quartos disponíveis
        """
        return [q for q in self._quartos if q.disponivel]


class ReservaService:
    """
    Serviço para gerenciamento de reservas.
    
    Responsável por criar, listar e gerenciar reservas de quartos.
    """
    
    def __init__(self):
        """Inicializa o serviço de reservas com lista vazia."""
        self._reservas = []
    
    @property
    def reservas(self):
        """Retorna a lista de reservas cadastradas."""
        return self._reservas
    
    def criarReserva(self, dataEntrada: date, dataSaida: date, 
                     cliente: Cliente, quarto: Quarto, idReserva: int = None) -> Reserva:
        """
        Cria e registra uma nova reserva.
        
        Args:
            dataEntrada (date): Data de check-in
            dataSaida (date): Data de check-out
            cliente (Cliente): Cliente que faz a reserva
            quarto (Quarto): Quarto a ser reservado
            idReserva (int, optional): ID da reserva
        
        Returns:
            Reserva: Objeto reserva criado
        
        Raises:
            ValueError: Se datas forem inválidas
            Exception: Se quarto não estiver disponível
        """
        # Cria a reserva (validações são feitas no construtor)
        reserva = Reserva(dataCheckin=dataEntrada, dataCheckout=dataSaida,
                         cliente=cliente, quarto=quarto, idReserva=idReserva)
        
        self._reservas.append(reserva)
        return reserva
    
    def listarReservas(self):
        """
        Lista todas as reservas cadastradas.
        
        Returns:
            list: Lista de reservas
        """
        return self._reservas
    
    def cancelar(self, reserva: Reserva) -> str:
        """
        Cancela uma reserva.
        
        Args:
            reserva (Reserva): Reserva a ser cancelada
        
        Returns:
            str: Mensagem de resultado
        """
        if reserva in self._reservas:
            reserva.cancelarReserva()
            self._reservas.remove(reserva)
            return "Reserva cancelada com sucesso!"
        return "Reserva não encontrada."
    
    def buscarPorCliente(self, cliente: Cliente):
        """
        Busca reservas de um cliente específico.
        
        Args:
            cliente (Cliente): Cliente a buscar
        
        Returns:
            list: Lista de reservas do cliente
        """
        return [r for r in self._reservas if r.cliente == cliente]
    
    def buscarPorId(self, id_reserva: int):
        """
        Busca uma reserva pelo ID.
        
        Args:
            id_reserva (int): ID da reserva
        
        Returns:
            Reserva: Reserva encontrada ou None
        """
        for reserva in self._reservas:
            if reserva.idReserva == id_reserva:
                return reserva
        return None
