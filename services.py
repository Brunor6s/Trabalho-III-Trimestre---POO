from classes import Cliente, Funcionario, Quarto, Reserva
import re

# Funções de validação simples
def validar_nome(nome: str):
    if not nome or not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    return nome.strip()

def validar_documento(doc: str):
    # aceita somente dígitos e no máximo 11 caracteres (CPF simplificado)
    if not doc:
        raise ValueError("Documento (CPF) é obrigatório.")
    doc_clean = re.sub(r"\D", "", doc)  # remove não dígitos
    if len(doc_clean) == 0 or len(doc_clean) > 11:
        raise ValueError("Documento (CPF) inválido: deve ter até 11 dígitos numéricos.")
    return doc_clean

def validar_email(email: str):
    if not email or "@" not in email:
        raise ValueError("Email inválido.")
    # validação simples: algo@algo.dom
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Email inválido.")
    return email.strip()

def validar_telefone(tel: str):
    if not tel:
        raise ValueError("Telefone é obrigatório.")
    tel_clean = tel.strip()
    # permitir dígitos e traço
    if not re.match(r"^[0-9\-]+$", tel_clean):
        raise ValueError("Telefone inválido: use apenas dígitos e '-'")
    digits = re.sub(r"\D", "", tel_clean)
    if len(digits) < 8:
        raise ValueError("Telefone inválido: deve ter no mínimo 8 dígitos.")
    return tel_clean

# Serviços
class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrarCliente(self, cliente: Cliente, autor="dono"):
        # autor aceita 'dono' ou 'funcionario'
        if autor not in ["dono", "funcionario"]:
            raise PermissionError("Apenas DONO ou FUNCIONÁRIO podem cadastrar clientes.")

        # validações
        validar_nome(cliente.nome)
        cliente.documento = validar_documento(cliente.documento)
        validar_email(cliente.email)
        cliente.telefone = validar_telefone(cliente.telefone)

        # opcional: evitar CPF duplicado
        for c in self.clientes:
            if c.documento == cliente.documento:
                raise ValueError("Já existe cliente com este documento (CPF).")

        self.clientes.append(cliente)
        return "Cliente cadastrado com sucesso!"

    def listarClientes(self):
        return self.clientes


class FuncionarioService:
    def __init__(self):
        self.funcionarios = []

    def cadastrarFuncionario(self, funcionario: Funcionario, autor="dono"):
        # somente dono pode cadastrar funcionário
        if autor != "dono":
            raise PermissionError("Apenas o DONO pode cadastrar funcionários.")

        # validações
        validar_nome(funcionario.nome)
        funcionario.documento = validar_documento(funcionario.documento)
        validar_email(funcionario.email)

        # evitar documento duplicado
        for f in self.funcionarios:
            if f.documento == funcionario.documento:
                raise ValueError("Já existe funcionário com este documento (CPF).")

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
        # alias usado no código
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
        # cria e retorna objeto Reserva (vai validar datas no construtor)
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
