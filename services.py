from classes import Cliente, Funcionario, Quarto, Reserva

class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrarCliente(self, cliente: Cliente):
        # Removido requisito de 'usuario_logado'
        self.clientes.append(cliente)
        return "Cliente cadastrado com sucesso!"

    def listarClientes(self):
        return self.clientes

class FuncionarioService:
    def __init__(self):
        self.funcionarios = []

    def cadastrarFuncionario(self, funcionario: Funcionario):
        # Removido requisito de 'usuario_logado'
        self.funcionarios.append(funcionario)
        return "Funcionário cadastrado com sucesso!"

    def listarFuncionarios(self):
        return self.funcionarios

class QuartoService:
    def __init__(self):
        self.quartos = []

    def adicionarQuarto(self, quarto: Quarto):
        self.quartos.append(quarto)
        return "Quarto adicionado com sucesso!"

    cadastrarQuarto = adicionarQuarto  # alias, caso o código chame por outro nome

    def listarQuartos(self):
        return self.quartos

    def buscarDisponivel(self):
        for quarto in self.quartos:
            if quarto.disponivel:
                return quarto
        return None

class ReservaService:
    def __init__(self):
        self.reservas = []

    def criarReserva(self, idReserva, dataEntrada, dataSaida, cliente, quarto):
        reserva = Reserva(idReserva, dataEntrada, dataSaida, cliente, quarto)
        self.reservas.append(reserva)
        return reserva

    def listarReservas(self):
        return self.reservas

    def cancelar(self, reserva):
        if reserva in self.reservas:
            reserva.cancelarReserva()  # libera o quarto
            self.reservas.remove(reserva)
            return "Reserva cancelada."
        return "Reserva não encontrada."
