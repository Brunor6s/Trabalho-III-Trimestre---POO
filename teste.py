"""
Módulo de testes - Testa as funcionalidades do sistema de hotel.

Este arquivo contém testes para validar o funcionamento correto das classes
e serviços do sistema de reservas de hotel.
"""

from datetime import date, timedelta
from models import Cliente, Funcionario, Quarto, Reserva
from services import ClienteService, FuncionarioService, QuartoService, ReservaService


def testar_cliente():
    """Testa a criação e validação de clientes."""
    print("=" * 50)
    print("TESTE: Cliente")
    print("=" * 50)
    
    try:
        # Teste 1: Cliente válido
        cliente = Cliente(
            nome="Maria Silva",
            documento="12345678901",
            email="maria@email.com",
            telefone="(11) 98765-4321",
            senha="senha123"
        )
        cliente.exibirDados()
        print(f"✓ Cliente criado com sucesso: {cliente}")
        
        # Teste 2: Validação de telefone
        try:
            cliente.telefone = "123"  # Telefone inválido
            print("✗ ERRO: Telefone inválido deveria falhar")
        except ValueError as e:
            print(f"✓ Validação de telefone funcionando: {e}")
        
        # Teste 3: Validação de email
        try:
            cliente2 = Cliente("João", "98765432100", "email_invalido", "(11) 99999-9999", "123")
            print("✗ ERRO: Email inválido deveria falhar")
        except ValueError as e:
            print(f"✓ Validação de email funcionando: {e}")
        
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de cliente: {e}")
        print()


def testar_funcionario():
    """Testa a criação e validação de funcionários."""
    print("=" * 50)
    print("TESTE: Funcionário")
    print("=" * 50)
    
    try:
        # Teste 1: Funcionário válido
        func = Funcionario(
            nome="Maurício de Souza",
            documento="11122233344",
            email="mauricio@hotel.com",
            cargo="Recepcionista",
            senha="func123"
        )
        func.exibirDados()
        print(f"✓ Funcionário criado com sucesso: {func}")
        
        # Teste 2: Revisão de quarto
        resultado = func.revisarQuarto()
        if resultado:
            print("✓ Método revisarQuarto funcionando")
        
        # Teste 3: Validação de cargo vazio
        try:
            func.cargo = ""
            print("✗ ERRO: Cargo vazio deveria falhar")
        except ValueError as e:
            print(f"✓ Validação de cargo funcionando: {e}")
        
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de funcionário: {e}")
        print()


def testar_quarto():
    """Testa a criação e gerenciamento de quartos."""
    print("=" * 50)
    print("TESTE: Quarto")
    print("=" * 50)
    
    try:
        # Teste 1: Quarto válido
        quarto = Quarto(numero=101, tipo="Luxo", precoDiaria=250.50)
        print(f"✓ Quarto criado: {quarto}")
        
        # Teste 2: Marcar ocupado
        quarto.marcarOcupado()
        if not quarto.disponivel:
            print("✓ Quarto marcado como ocupado")
        
        # Teste 3: Liberar quarto
        quarto.liberarQuarto()
        if quarto.disponivel:
            print("✓ Quarto liberado com sucesso")
        
        # Teste 4: Validação de preço negativo
        try:
            quarto2 = Quarto(numero=102, tipo="Solteiro", precoDiaria=-100)
            print("✗ ERRO: Preço negativo deveria falhar")
        except ValueError as e:
            print(f"✓ Validação de preço funcionando: {e}")
        
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de quarto: {e}")
        print()


def testar_reserva():
    """Testa a criação e gerenciamento de reservas."""
    print("=" * 50)
    print("TESTE: Reserva")
    print("=" * 50)
    
    try:
        # Criar objetos necessários
        cliente = Cliente("Ana Costa", "55566677788", "ana@email.com", "(11) 91111-2222", "ana123")
        quarto = Quarto(numero=201, tipo="Suite", precoDiaria=350.0)
        
        hoje = date.today()
        checkin = hoje + timedelta(days=1)
        checkout = hoje + timedelta(days=4)
        
        # Teste 1: Reserva válida
        reserva = Reserva(
            dataCheckin=checkin,
            dataCheckout=checkout,
            cliente=cliente,
            quarto=quarto
        )
        print(f"✓ Reserva criada: {reserva}")
        
        # Teste 2: Cálculo de valor
        valor_esperado = 3 * 350.0  # 3 dias * R$350
        if reserva.valorTotal == valor_esperado:
            print(f"✓ Valor total calculado corretamente: R$ {reserva.valorTotal:.2f}")
        else:
            print(f"✗ ERRO: Valor incorreto. Esperado: {valor_esperado}, Obtido: {reserva.valorTotal}")
        
        # Teste 3: Quarto deve estar ocupado
        if not quarto.disponivel:
            print("✓ Quarto marcado como ocupado após reserva")
        
        # Teste 4: Cancelar reserva
        reserva.cancelarReserva()
        if quarto.disponivel:
            print("✓ Quarto liberado após cancelamento")
        
        # Teste 5: Validação de datas inválidas
        try:
            quarto2 = Quarto(numero=202, tipo="Casal", precoDiaria=200.0)
            reserva_invalida = Reserva(checkout, checkin, cliente, quarto2)  # Datas invertidas
            print("✗ ERRO: Datas invertidas deveriam falhar")
        except ValueError as e:
            print(f"✓ Validação de datas funcionando: {e}")
        
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de reserva: {e}")
        print()


def testar_services():
    """Testa os serviços de gerenciamento."""
    print("=" * 50)
    print("TESTE: Services")
    print("=" * 50)
    
    try:
        # Inicializar serviços
        cliente_service = ClienteService()
        func_service = FuncionarioService()
        quarto_service = QuartoService()
        reserva_service = ReservaService()
        
        # Teste ClienteService
        cliente1 = cliente_service.criar("Roberto Lima", "11111111111", "roberto@email.com", "senha1", "(11) 99999-8888")
        print(f"✓ Cliente cadastrado via service: {cliente1.nome}")
        
        # Teste duplicação de CPF
        try:
            cliente_service.criar("Darlan Romani", "11111111111", "darlanromani@email.com", "senha2")
            print("✗ ERRO: CPF duplicado deveria falhar")
        except ValueError as e:
            print(f"✓ Validação de CPF duplicado funcionando: {e}")
        
        # Teste FuncionarioService
        func1 = func_service.criar("Julia Oliveira", "julia@hotel.com", "julia123", "22222222222", "Gerente")
        print(f"✓ Funcionário cadastrado via service: {func1.nome}")
        
        # Teste permissão (somente dono pode cadastrar funcionário)
        try:
            func_service.criar("Teste", "teste@hotel.com", "123", "33333333333", "Cargo", autor="cliente")
            print("✗ ERRO: Cliente não deveria poder cadastrar funcionário")
        except PermissionError as e:
            print(f"✓ Validação de permissão funcionando: {e}")
        
        # Teste QuartoService
        quarto1 = quarto_service.criar("301", "400.00", "Presidencial")
        print(f"✓ Quarto cadastrado via service: Quarto {quarto1.numero}")
        
        # Teste buscar quarto disponível
        quarto_disp = quarto_service.buscarDisponivel()
        if quarto_disp:
            print(f"✓ Quarto disponível encontrado: {quarto_disp.numero}")
        
        # Teste ReservaService
        hoje = date.today()
        reserva1 = reserva_service.criarReserva(
            hoje + timedelta(days=2),
            hoje + timedelta(days=5),
            cliente1,
            quarto1
        )
        print(f"✓ Reserva criada via service: ID {reserva1.idReserva}")
        
        # Listar reservas
        reservas = reserva_service.listarReservas()
        print(f"✓ Total de reservas: {len(reservas)}")
        
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de services: {e}")
        print()


def testar_heranca_polimorfismo():
    """Testa herança e polimorfismo."""
    print("=" * 50)
    print("TESTE: Herança e Polimorfismo")
    print("=" * 50)
    
    try:
        # Criar lista de pessoas (polimorfismo)
        pessoas = []
        pessoas.append(Cliente("Cliente 1", "12312312312", "c1@email.com", "(11) 91111-1111", "123"))
        pessoas.append(Funcionario("Funcionario 1", "32132132132", "f1@email.com", "Limpeza", "456"))
        
        # Testar método polimórfico exibirDados
        print("Testando polimorfismo (método exibirDados):")
        for pessoa in pessoas:
            print(f"\nTipo: {type(pessoa).__name__}")
            pessoa.exibirDados()
        
        print("\n✓ Herança e polimorfismo funcionando corretamente")
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de herança: {e}")
        print()


def testar_encapsulamento():
    """Testa encapsulamento com properties."""
    print("=" * 50)
    print("TESTE: Encapsulamento (Properties)")
    print("=" * 50)
    
    try:
        cliente = Cliente("Teste Encap", "99988877766", "teste@email.com", "(11) 98888-7777", "senha")
        
        # Teste 1: Acesso via property
        print(f"Nome (via property): {cliente.nome}")
        print(f"Email (via property): {cliente.email}")
        
        # Teste 2: Modificação via property (com validação)
        cliente.nome = "Novo Nome"
        print(f"✓ Nome alterado via property: {cliente.nome}")
        
        # Teste 3: Validação ao modificar
        try:
            cliente.email = "email_sem_arroba"
            print("✗ ERRO: Email inválido deveria falhar")
        except ValueError as e:
            print(f"✓ Property validando corretamente: {e}")
        
        # Teste 4: Atributos privados não devem ser acessados diretamente
        print(f"✓ Atributos privados protegidos: _nome = {cliente._nome}")
        print("  (Acesso direto possível em Python, mas desencorajado)")
        
        print()
        
    except Exception as e:
        print(f"✗ ERRO no teste de encapsulamento: {e}")
        print()


def executar_todos_testes():
    """Executa todos os testes do sistema."""
    print("\n")
    print("=" * 50)
    print("  SISTEMA DE TESTES - HOTEL POO")
    print("=" * 50)
    print()
    
    testar_cliente()
    testar_funcionario()
    testar_quarto()
    testar_reserva()
    testar_services()
    testar_heranca_polimorfismo()
    testar_encapsulamento()
    
    print("=" * 50)
    print("TESTES CONCLUIDOS")
    print("=" * 50)


if __name__ == "__main__":
    executar_todos_testes()
