from services import criar_pessoa, listar_pessoas, criar_imovel, listar_imoveis, criar_anuncio, listar_anuncios

# Menu sistema de hotel
def menu():
    print("\n=== Sistema de Testes ===")
    print("1. Criar Pessoa")
    print("2. Listar Pessoas")
    print("3. Criar Imóvel")
    print("4. Listar Imóveis")
    print("5. Criar Anúncio")
    print("6. Listar Anúncios")
    print("0. Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da pessoa: ")
            email = input("Email da pessoa: ")
            criar_pessoa(nome, email)
            print("Pessoa criada com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de Pessoas ---")
            for p in listar_pessoas():
                print(f"ID: {p.id} | Nome: {p.nome} | Email: {p.email}")

        elif opcao == "3":
            endereco = input("Endereço do imóvel: ")
            preco = float(input("Preço da diária: "))
            criar_imovel(endereco, preco)
            print("Imóvel criado com sucesso!")

        elif opcao == "4":
            print("\n--- Lista de Imóveis ---")
            for i in listar_imoveis():
                print(f"ID: {i.id} | Endereço: {i.endereco} | Preço: {i.preco}")

        elif opcao == "5":
            imovel_id = int(input("ID do imóvel para anúncio: "))
            titulo = input("Título do anúncio: ")
            criar_anuncio(imovel_id, titulo)
            print("Anúncio criado com sucesso!")

        elif opcao == "6":
            print("\n--- Lista de Anúncios ---")
            for a in listar_anuncios():
                print(f"ID: {a.id} | Título: {a.titulo} | Imóvel: {a.imovel_id}")

        elif opcao == "0":
            print("Sair")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
