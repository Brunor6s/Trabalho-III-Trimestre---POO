from services import criar_pessoa, listar_pessoas, criar_imovel, listar_imoveis, criar_anuncio, listar_anuncios

# Menu do sistema de hotel
def menu():
    print("=== Sistema de Testes ===")
    print("1. Criar Pessoa")
    print("2. Listar Pessoas")
    print("3. Criar Imóvel")
    print("4. Listar Imóveis")
    print("5. Criar Anúncio")
    print("6. Listar Anúncios")
    print("0. Sair")


def main():
    print("=== SISTEMA DE HOTEL ===")

    usuarios = {
        "c": {"senha": "123", "tipo": "cliente"},
        "f": {"senha": "123", "tipo": "funcionario"},
        "d": {"senha": "123", "tipo": "dono"},
    }

    nome = input("Usuário (c/f/d): ")
    senha = input("Senha: ")

    if nome not in usuarios or usuarios[nome]["senha"] != senha:
        print("Login inválido.")
        return

    tipo = usuarios[nome]["tipo"]
    print(f"Login efetuado, tipo de usuário: {tipo.upper()}")

    servico = ServicoReserva()
    cliente_teste = Cliente("João", "123456", "joao@gmail.com", 1, "9999-9999")
    funcionario_teste = Funcionario("Pedro", "999888", "pedro@hotel.com", 1, "Recepção")
    dono_teste = Funcionario("Mario", "888777", "mario@hotel.com", 2, "Dono")
    quarto101 = Quarto(101, "Luxo", 200.0)

    if tipo == "cliente":
        menu_cliente(servico, cliente_teste, quarto101)
    elif tipo == "funcionario":
        menu_funcionario(servico, funcionario_teste, quarto101)
    elif tipo == "dono":
        menu_dono(servico, dono_teste, quarto101)

    print("Sistema finalizado.")

if __name__ == "__main__":
    main()
