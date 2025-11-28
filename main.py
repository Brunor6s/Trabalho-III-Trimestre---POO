from datetime import date, datetime
from classes import Cliente, Funcionario, Quarto
from services import ClienteService, FuncionarioService, QuartoService, ReservaService

def ler_data(prompt):
    s = input(prompt + " (formato YYYY-MM-DD): ")
    try:
        y, m, d = map(int, s.split("-"))
        return date(y, m, d)
    except Exception:
        print("Formato inválido, usando data de hoje.")
        return date.today()

def menu_cliente(serv_reserva: ReservaService, cliente: Cliente, serv_quarto: QuartoService):
    while True:
        print("\n--- MENU CLIENTE ---")
        print("1. Ver quartos disponíveis")
        print("2. Fazer reserva")
        print("3. Minhas reservas")
        print("0. Logout")
        op = input("Escolha: ")

        if op == "1":
            print("\n--- QUARTOS DISPONÍVEIS ---")
            encontrou = False
            for q in serv_quarto.quartos:
                if q.disponivel:
                    print(f"Quarto {q.numero} | Tipo: {q.tipo} | Preço: R$ {q.precoDiaria:.2f}")
                    encontrou = True
            if not encontrou:
                print("Nenhum quarto disponível no momento.")

        elif op == "2":
            quarto = serv_quarto.buscarDisponivel()
            if not quarto:
                print("Nenhum quarto disponível no momento.")
                continue

            print(f"Quarto disponível: {quarto.numero} | Tipo: {quarto.tipo} | Preço: R$ {quarto.precoDiaria:.2f}")
            checkin = ler_data("Data de check-in")
            checkout = ler_data("Data de check-out")

            if checkout <= checkin:
                print("Check-out deve ser depois do check-in.")
                continue

            idReserva = int(datetime.now().timestamp()) % 100000
            reserva = serv_reserva.criarReserva(idReserva, checkin, checkout, cliente, quarto)

            if reserva:
                total = reserva.calcularTotal()
                print(f"Reserva criada. Total: R$ {total:.2f}")

        elif op == "3":
            print("\n--- Minhas reservas ---")
            encontrou = False
            for r in serv_reserva.reservas:
                if r.cliente.nome == cliente.nome:
                    print(f"Reserva {r.idReserva} - Quarto {r.quarto.numero} - {r.dataCheckin} a {r.dataCheckout} - Total: R$ {r.valorTotal:.2f}")
                    encontrou = True
            if not encontrou:
                print("Nenhuma reserva encontrada para você.")

        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu_funcionario(serv_reserva: ReservaService, serv_quarto: QuartoService, funcionario: Funcionario, serv_cliente: ClienteService):
    while True:
        print("\n--- MENU FUNCIONÁRIO ---")
        print("1. Listar reservas")
        print("2. Cancelar reserva (por id)")
        print("3. Listar quartos")
        print("4. Marcar quarto como liberado")
        print("5. Cadastrar cliente")  
        print("0. Logout")


        if op == "1":
            print("\n--- RESERVAS ---")
            if serv_reserva.reservas:
                for r in serv_reserva.reservas:
                    print(f"Reserva {r.idReserva} - Quarto {r.quarto.numero} - {r.dataCheckin} a {r.dataCheckout} - Total: R$ {r.valorTotal:.2f}")
            else:
                print("Não há reservas cadastradas.")

        elif op == "2":
            try:
                idr = int(input("ID da reserva para cancelar: "))
            except:
                print("ID inválido.")
                continue

            alvo = None
            for r in serv_reserva.reservas:
                if r.idReserva == idr:
                    alvo = r
                    break

            if not alvo:
                print("Reserva não encontrada.")
            else:
                serv_reserva.cancelar(alvo)
                print("Reserva cancelada com sucesso.")

        elif op == "3":
            print("\n--- QUARTOS ---")
            if serv_quarto.quartos:
                for q in serv_quarto.quartos:
                    status = "Disponível" if q.disponivel else "Ocupado"
                    print(f"Quarto {q.numero} - {q.tipo} - R$ {q.precoDiaria:.2f} - {status}")
            else:
                print("Nenhum quarto cadastrado.")

        elif op == "4":
            try:
                num = int(input("Número do quarto para liberar: "))
            except:
                print("Número inválido.")
                continue

            achou = False
            for q in serv_quarto.quartos:
                if q.numero == num:
                    q.liberarQuarto()
                    print(f"Quarto {num} liberado.")
                    achou = True
                    break

            if not achou:
                print("Quarto não encontrado.")

        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu_dono(serv_cliente: ClienteService, serv_func: FuncionarioService, serv_quarto: QuartoService, serv_reserva: ReservaService):
    while True:
        print("\n--- MENU DONO ---")
        print("1. Cadastrar funcionário")
        print("2. Listar funcionários")
        print("3. Adicionar quarto")
        print("4. Listar quartos")
        print("5. Listar clientes")
        print("6. Listar reservas")
        print("0. Logout")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome do funcionário: ")
            doc = input("Documento: ")
            email = input("Email: ")
            try:
                idf = int(input("ID do funcionário: "))
            except:
                idf = len(serv_func.funcionarios) + 1
            cargo = input("Cargo: ")

            f = Funcionario(nome, doc, email, idf, cargo)
            serv_func.cadastrarFuncionario(f)
            print("Funcionário cadastrado com sucesso.")

        elif op == "2":
            print("\n--- FUNCIONÁRIOS ---")
            if serv_func.funcionarios:
                for f in serv_func.funcionarios:
                    print(f"Funcionário {f.idFuncionario} - {f.nome} - {f.cargo}")
            else:
                print("Nenhum funcionário cadastrado.")

        elif op == "3":
            try:
                numero = int(input("Número do quarto: "))
            except:
                print("Número inválido.")
                continue

            tipo = input("Tipo do quarto: ")
            try:
                preco = float(input("Preço da diária: "))
            except:
                preco = 0.0

            q = Quarto(numero, tipo, preco)
            serv_quarto.adicionarQuarto(q)
            print("Quarto adicionado com sucesso.")

        elif op == "4":
            print("\n--- QUARTOS ---")
            if serv_quarto.quartos:
                for q in serv_quarto.quartos:
                    status = "Disponível" if q.disponivel else "Ocupado"
                    print(f"Quarto {q.numero} - {q.tipo} - R$ {q.precoDiaria:.2f} - {status}")
            else:
                print("Nenhum quarto cadastrado.")

        elif op == "5":
            print("\n--- CLIENTES ---")
            if serv_cliente.clientes:
                for c in serv_cliente.clientes:
                    print(f"Cliente {c.idCliente} - {c.nome} - {c.telefone}")
            else:
                print("Nenhum cliente cadastrado.")

        elif op == "6":
            print("\n--- RESERVAS ---")
            if serv_reserva.reservas:
                for r in serv_reserva.reservas:
                    print(f"Reserva {r.idReserva} - Quarto {r.quarto.numero} - {r.dataCheckin} a {r.dataCheckout} - Total: R$ {r.valorTotal:.2f}")
            else:
                print("Nenhuma reserva cadastrada.")

        elif op == "0":
            break
        else:
            print("Opção inválida.")

def main():
    print("=== SISTEMA DE HOTEL ===")

    serv_cliente = ClienteService()
    serv_func = FuncionarioService()
    serv_quarto = QuartoService()
    serv_reserva = ReservaService()

    usuarios = {
        "c": {"senha": "123", "tipo": "cliente"},
        "f": {"senha": "123", "tipo": "funcionario"},
        "d": {"senha": "123", "tipo": "dono"},
    }

    cliente_ex = Cliente("João", "123456", "joao@gmail.com", 1, "9999-9999")
    serv_cliente.cadastrarCliente(cliente_ex)

    func_ex = Funcionario("Pedro", "999888", "pedro@hotel.com", 1, "Recepção")
    serv_func.cadastrarFuncionario(func_ex)

    serv_quarto.adicionarQuarto(Quarto(101, "Solteiro", 150.0))
    serv_quarto.adicionarQuarto(Quarto(102, "Casal", 200.0))

    usuario = input("Usuário (c/f/d): ")
    senha = input("Senha: ")

    if usuario not in usuarios or usuarios[usuario]["senha"] != senha:
        print("Login inválido.")
        return

    tipo = usuarios[usuario]["tipo"]
    print(f"Login efetuado. Tipo: {tipo.upper()}")

    if tipo == "cliente":
        menu_cliente(serv_reserva, cliente_ex, serv_quarto)
    elif tipo == "funcionario":
        menu_funcionario(serv_reserva, serv_quarto, func_ex)
    elif tipo == "dono":
        menu_dono(serv_cliente, serv_func, serv_quarto, serv_reserva)

    print("Sistema finalizado.")

if __name__ == "__main__":
    main()
