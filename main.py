"""
Ponto de Entrada do Sistema de Hotel.
Realiza a composição de todos os serviços seguindo o Princípio DIP.
"""
from services import ClienteService, FuncionarioService, QuartoService, ReservaService, FinanceiroService
from interface import HotelApp
from models.cliente import Cliente

# 1. Repositórios (Persistência em Memória - DIP)
db_clientes = []
db_funcionarios = []
db_quartos = []
db_reservas = []

# 2. Inicialização dos Serviços (DIP/SRP)
serv_financeiro = FinanceiroService()
serv_cliente = ClienteService(db_clientes)
serv_func = FuncionarioService(db_funcionarios)
serv_quarto = QuartoService(db_quartos)
serv_reserva = ReservaService(db_reservas, serv_financeiro)

# 3. Carga Inicial de Dados
def carregar_dados_teste():
    # Cadastro de um cliente inicial
    c1 = Cliente("Jordan Kuhn", "12345678901", "jordan@gmail.com", "11988887777", "123")
    serv_cliente.cadastrarCliente(c1)
    
    # Cadastro de Quartos Polimórficos
    serv_quarto.criar(101, "Solteiro")
    serv_quarto.criar(102, "Casal")
    serv_quarto.criar(201, "Luxo")
    serv_quarto.criar(301, "Presidencial")

if __name__ == "__main__":
    carregar_dados_teste()
    
    print("[SISTEMA] Iniciando HotelApp...")
    # Passamos os serviços configurados para a interface
    app = HotelApp(serv_cliente, serv_func, serv_quarto, serv_reserva)
    app.run()