from classes import Cliente, Funcionario, Quarto, Reserva

class ClienteService:
    def __init__(self):
        self.clientes = []

    class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrarCliente(self, cliente: Cliente, autor="dono"):
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem cadastrar clientes.")

        self.clientes.append(cliente)
        return "Cliente cadastrado com sucesso!"

    def listarClientes(self):
        return self.clientes

    def listarClientes(self):
        return self.clientes

class FuncionarioService:
    def __init__(self):
        self.funcionarios = []

    def cadastrarFuncionario(self, funcionario: Funcionario):
        # Cadastro permitido sem verificação extra
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

    def adicionarQuarto(self, quarto: Quarto):
        # Alias para cadastrarQuarto (usado no código principal)
        return self.cadastrarQuarto(quarto)

    def listarQuartos(self):
        return self.quartos

    def buscarDisponivel(self):
        for q in self.quartos:
            if q.disponivel:
                return q
        return None

class ReservaService:
    def __init__(self):
        self.reservas = []

    def criarReserva(self, idReserva, dataEntrada, dataSaida, cliente: Cliente, quarto: Quarto):
        reserva = Reserva(idReserva, dataEntrada, dataSaida, cliente, quarto)
        self.reservas.append(reserva)
        return reserva

    def listarReservas(self):
        return self.reservas

    def cancelar(self, reserva: Reserva):
        if reserva in self.reservas:
            reserva.cancelarReserva()
            self.reservas.remove(reserva)
            return "Reserva cancelada com sucesso!"
        return "Reserva não encontrada."
