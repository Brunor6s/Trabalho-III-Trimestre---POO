from classes import Cliente, Funcionario, Quarto, Reserva


class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrarCliente(self, cliente: Cliente):
        if self.usuario_logado["tipo"] != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar novos clientes.")

        self.clientes.append(cliente)
        return "Cliente cadastrado com sucesso!"

    def listarClientes(self):
        return self.clientes


class FuncionarioService:
    def __init__(self):
        self.funcionarios = []

    def cadastrarFuncionario(self, funcionario: Funcionario):
        if self.usuario_logado["tipo"] != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar novos funcionários.")

        self.funcionarios.append(funcionario)
        return "Funcionário cadastrado com sucesso!"

    def listarFuncionarios(self):
        return self.funcionarios


class QuartoService:
    def __init__(self):
        self.quartos = []

    def cadastrarQuarto(self, quarto: Quarto):
        self.quartos.append(quarto)
        return "Quarto cadastrado com sucesso!"

    def listarQuartos(self):
        return self.quartos


class ReservaService:
    def __init__(self):
        self.reservas = []

    def criarReserva(self, reserva: Reserva):
        self.reservas.append(reserva)
        return "Reserva criada com sucesso!"

    def listarReservas(self):
        return self.reservas
