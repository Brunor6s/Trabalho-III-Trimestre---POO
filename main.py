"""
Sistema de Reservas de Hotel - Arquivo Principal

Este módulo inicializa o sistema com dados de exemplo e executa a interface gráfica moderna.
"""

from models import Cliente, Funcionario, Quarto
from services import ClienteService, FuncionarioService, QuartoService, ReservaService
from interface import HotelApp

# Inicialização dos serviços e dados
serv_cliente = ClienteService()
serv_func = FuncionarioService()
serv_quarto = QuartoService()
serv_reserva = ReservaService()

# Criando exemplo de cliente (com senha)
cliente_ex = Cliente(nome="Jordan Kuhn", documento="12345678900", email="jordan@gmail.com", 
                    telefone="(11) 9999-9999", senha="123")
serv_cliente.cadastrarCliente(cliente_ex, autor="dono")

# Criando exemplo de funcionário (com senha)
func_ex = Funcionario(nome="Bruno Reis", documento="98765432100", email="bruno@hotel.com", 
                     cargo="Recepção", senha="123")
serv_func.cadastrarFuncionario(func_ex, autor="dono")

# Criando exemplo de quartos
serv_quarto.adicionarQuarto(Quarto(numero=101, tipo="Solteiro", precoDiaria=150.0))
serv_quarto.adicionarQuarto(Quarto(numero=102, tipo="Casal", precoDiaria=200.0))
serv_quarto.adicionarQuarto(Quarto(numero=201, tipo="Luxo", precoDiaria=300.0))
serv_quarto.adicionarQuarto(Quarto(numero=202, tipo="Suite", precoDiaria=400.0))
serv_quarto.adicionarQuarto(Quarto(numero=301, tipo="Presidencial", precoDiaria=600.0))

# Execução da aplicação gráfica
if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA DE HOTEL - GESTÃO DE RESERVAS")
    print("=" * 50)
    print("\n💡 Credenciais de Acesso:")
    print("-" * 50)
    print("📌 DONO:")
    print("   Email: dono")
    print("   Senha: 123")
    print()
    print(f"📌 FUNCIONÁRIO:")
    print(f"   Email: {func_ex.email}")
    print(f"   Senha: 123")
    print()
    print(f"📌 CLIENTE:")
    print(f"   Email: {cliente_ex.email}")
    print(f"   Senha: 123")
    print("=" * 50)
    print("\nIniciando interface gráfica...\n")
    
    # Criar e executar aplicação
    app = HotelApp(serv_cliente, serv_func, serv_quarto, serv_reserva)
    app.run()
