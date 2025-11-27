from classes import Cliente, Funcionario, Quarto, Reserva
from datetime import date

class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
    if self.usuario_logado["tipo"] != "dono" or "funcionario":
        messagebox.showerror("Acesso negado", "Apenas o dono pode cadastrar clientes!")
        return


    def listarClientes(self):
        if not self.clientes:
            return "Nenhum cliente cadastrado."

        texto = ""
        for c in self.clientes:
            texto += (
                f"Cliente:\n"
                f"Nome: {c.nome}\n"
                f"Documento: {c.documento}\n"
                f"Email: {c.email}\n"
                f"Telefone: {c.telefone}\n"
                f"-----------------------------\n"
            )
        return texto


class QuartoService:
    def __init__(self):
        self.quartos = []

    def adicionarQuarto(self, quarto: Quarto):
        self.quartos.append(quarto)
        return "Quarto adicionado!"

    def listarQuartos(self):
        if not self.quartos:
            return "Nenhum quarto cadastrado."

        texto = ""
        for q in self.quartos:
            texto += (
                f"Quarto {q.numero} | Tipo: {q.tipo} | "
                f"Disponível: {'Sim' if q.disponivel else 'Não'}\n"
            )
        return texto

    def buscarDisponivel(self):
        for q in self.quartos:
            if q.disponivel:
                return q
        return None


class ReservaService:
    def __init__(self):
        self.reservas = []

    def criarReserva(self, idReserva, checkin, checkout, cliente, quarto):
        try:
            reserva = Reserva(idReserva, checkin, checkout, cliente, quarto)
            self.reservas.append(reserva)
            return reserva
        except Exception as e:
            return None

    def listarReservas(self):
        if not self.reservas:
            return "Nenhuma reserva cadastrada."

        texto = ""
        for r in self.reservas:
            texto += (
                f"Reserva {r.idReserva} - Cliente: {r.cliente.nome} - "
                f"Quarto: {r.quarto.numero}\n"
            )
        return texto

    def cancelar(self, reserva: Reserva):
        if reserva in self.reservas:
            reserva.cancelarReserva()
            return "Reserva cancelada!"
        return "Reserva inexistente."


class FuncionarioService:
    def __init__(self):
        self.funcionarios = []

    def cadastrar_funcionario(self):
    if self.usuario_logado["tipo"] != "dono":
        messagebox.showerror("Acesso negado")
        return

    def listarFuncionarios(self):
        if not self.funcionarios:
            return "Nenhum funcionário cadastrado."

        texto = ""
        for f in self.funcionarios:
            texto += (
                f"Funcionário:\n"
                f"Nome: {f.nome}\n"
                f"Documento: {f.documento}\n"
                f"Email: {f.email}\n"
                f"Cargo: {f.cargo}\n"
                f"-----------------------------\n"
            )
        return texto
