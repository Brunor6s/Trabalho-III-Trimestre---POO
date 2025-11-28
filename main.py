from datetime import date, datetime
from classes import Cliente, Funcionario, Quarto
from services import ClienteService, FuncionarioService, QuartoService, ReservaService
from interface import Interface

# Inicialização dos serviços e dados
serv_cliente = ClienteService()
serv_func = FuncionarioService()
serv_quarto = QuartoService()
serv_reserva = ReservaService()

# Criando exemplo de cliente (com senha)
cliente_ex = Cliente(nome="João", documento="12345678900", email="joao@gmail.com", idCliente=1, telefone="9999-9999", senha="123")
serv_cliente.cadastrarCliente(cliente_ex, autor="dono")

# Criando exemplo de funcionário (com senha)
func_ex = Funcionario(nome="Pedro", documento="98765432100", email="pedro@hotel.com", idFuncionario=1, cargo="Recepção", senha="123")
serv_func.cadastrarFuncionario(func_ex, autor="dono")

# Criando exemplo de quartos
serv_quarto.adicionarQuarto(Quarto(numero=101, tipo="Solteiro", precoDiaria=150.0))
serv_quarto.adicionarQuarto(Quarto(numero=102, tipo="Casal", precoDiaria=200.0))
serv_quarto.adicionarQuarto(Quarto(numero=201, tipo="Luxo", precoDiaria=300.0))

# Execução da aplicação gráfica
if __name__ == "__main__":
    print("=== SISTEMA DE HOTEL (GUI) ===")
    app = Interface(serv_cliente, serv_func, serv_quarto)
    app.run()
