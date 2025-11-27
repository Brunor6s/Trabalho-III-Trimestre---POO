from classes import Cliente, Funcionario, Quarto, Reserva
from datetime import date

# Serviço de gerenciamento de clientes
class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrarCliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def listarClientes(self):
        for c in self.clientes:
            c.exibirDados()
            print("-------------------------")


# Serviço de gerenciamento de quartos
class QuartoService:
    def __init__(self):
        self.quartos = []

    def adicionarQuarto(self, quarto: Quarto):
        self.quartos.append(quarto)
        print("Quarto adicionado!")

    def listarQuartos(self):
        for q in self.quartos:
            print(f"Quarto {q.numero} | Tipo: {q.tipo} | Disponível: {q.disponivel}")

    def buscarDisponivel(self):
        for q in self.quartos:
            if q.disponivel:
                return q
        return None


# Serviço de reservas
class ReservaService:
    def __init__(self):
        self.reservas = []

    def criarReserva(self, idReserva, checkin, checkout, cliente, quarto):
        try:
            reserva = Reserva(idReserva, checkin, checkout, cliente, quarto)
            self.reservas.append(reserva)
            print("Reserva criada!")
            return reserva
        except Exception as e:
            print("Erro ao criar reserva:", e)
            return None

    def listarReservas(self):
        for r in self.reservas:
            print(f"Reserva {r.idReserva} - Cliente: {r.cliente.nome} - Quarto: {r.quarto.numero}")

    def cancelar(self, reserva: Reserva):
        if reserva in self.reservas:
            reserva.cancelarReserva()
            print("Reserva cancelada!")


# Serviço do Funcionário
class FuncionarioService:
    def __init__(self):
        self.funcionarios = []

    def cadastrarFuncionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
        print("Funcionário cadastrado!")

    def listarFuncionarios(self):
        for f in self.funcionarios:
            f.exibirDados()
            print("-------------------------")
