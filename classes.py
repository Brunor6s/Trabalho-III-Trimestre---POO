from abc import ABC, abstractmethod
from datetime import date

# Classe Abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome: str, documento: str, email: str):
        self.nome = nome
        self.documento = documento
        self.email = email

    @abstractmethod
    def exibirDados(self):
        pass

    def __str__(self):
        return f"{self.nome} - {self.documento} - {self.email}"


# Classe Cliente
class Cliente(Pessoa):
    def __init__(self, nome, documento, email, idCliente, telefone):
        super().__init__(nome, documento, email)
        self.idCliente = idCliente
        self.telefone = telefone

    def exibirDados(self):
        print("Cliente:")
        print("Nome:", self.nome)
        print("Documento:", self.documento)
        print("Email:", self.email)
        print("Telefone:", self.telefone)

    def solicitarReserva(self):
        print("Solicitando reserva...")

    def __str__(self):
        return f"Cliente {self.idCliente} - {self.nome} | {self.documento} | {self.email} | {self.telefone}"


# Classe Funcionário
class Funcionario(Pessoa):
    def __init__(self, nome, documento, email, idFuncionario, cargo):
        super().__init__(nome, documento, email)
        self.idFuncionario = idFuncionario
        self.cargo = cargo

    def exibirDados(self):
        print("Funcionário:")
        print("Nome:", self.nome)
        print("Documento:", self.documento)
        print("Email:", self.email)
        print("Cargo:", self.cargo)

    def revisarQuarto(self):
        print("Quarto revisado.")
        return True

    def __str__(self):
        return f"Funcionario {self.idFuncionario} - {self.nome} | {self.cargo} | {self.documento} | {self.email}"


# Classe Quarto
class Quarto:
    def __init__(self, numero: int, tipo: str, precoDiaria: float):
        self.numero = numero
        self.tipo = tipo
        self.precoDiaria = precoDiaria
        self.disponivel = True

    def marcarOcupado(self):
        self.disponivel = False

    def liberarQuarto(self):
        self.disponivel = True

    def revisarAposCheckout(self):
        print("Quarto precisa ser revisado após checkout.")
        return True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} - {self.tipo} - R$ {self.precoDiaria:.2f} - {status}"


# Classe Reserva
class Reserva:
    def __init__(self, idReserva: int, dataCheckin: date, dataCheckout: date, cliente: Cliente, quarto: Quarto):
        # validação de datas
        if dataCheckout <= dataCheckin:
            raise ValueError("Data de check-out deve ser posterior à data de check-in.")

        self.idReserva = idReserva
        self.dataCheckin = dataCheckin
        self.dataCheckout = dataCheckout
        self.valorTotal = 0.0
        self.cliente = cliente
        self.quarto = quarto

        if not quarto.disponivel:
            raise Exception("Quarto não está disponível.")

        quarto.marcarOcupado()

    def calcularTotal(self):
        dias = (self.dataCheckout - self.dataCheckin).days
        self.valorTotal = dias * self.quarto.precoDiaria
        return self.valorTotal

    def confirmarReserva(self):
        print("Reserva confirmada.")
        return True

    def cancelarReserva(self):
        print("Reserva cancelada.")
        self.quarto.liberarQuarto()
        return True

    def __str__(self):
        return f"Reserva {self.idReserva} - Cliente: {self.cliente.nome} - Quarto: {self.quarto.numero} - {self.dataCheckin} -> {self.dataCheckout} - Total: R$ {self.valorTotal:.2f}"
