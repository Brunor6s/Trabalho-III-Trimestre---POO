
Betano: 
from classes import (
    Locador, Locatario, Telefone, Foto, Amenidade, Avaliacao,
    Imovel, Anuncio, Contrato, Pagamento
)
from services import (
    ServicoLocador, ServicoLocatario, ServicoImovel,
    ServicoAvaliacao, ServicoAmenidade,
    ServicoAnuncio, ServicoContrato, ServicoPagamento
)
from datetime import date


def testar_locador_locatario():
    print("== Teste Pessoa / Locador / Locatário ==")

    locador = Locador("Maria", "Jobim", "dudajobim07@email.com",
                      "22/01/2007", "123456", 1, "10/10/2024",
                      "Conta X", 5)

    locatario = Locatario("Jordan", "Kuhn", "jordan_kuhn@email.com",
                          "05/03/2007", "654321", 2, "11/11/2024",
                          "Silencioso")

    print(locador.exibir_informacoes())
    print(locatario.exibir_informacoes())

    tel = Telefone("98461-3853")
    locador.adicionar_telefone(tel)

def testar_imovel():
    print("\n== Teste Imóvel ==")

    serv_imovel = ServicoImovel()

    imovel = Imovel(
        endereco="Rua Isidoro Maito, 25",
        status="Disponível",
        id_imovel=1,
        titulo="Apartamento Centro",
        descricao="1 quarto",
        tipo="Apartamento",
        area_m2=40,
        valor_aluguel=1500
    )

    foto = Foto("caminho/foto1.jpg")
    amenidade = Amenidade(1, "Piscina")
    avaliacao = Avaliacao(1, 5, "Ótimo lugar", "10/10/2024")

    imovel.adicionar_foto(foto)
    imovel.adicionar_amenidade(amenidade)
    imovel.adicionar_avaliacao(avaliacao)

    print("Imóvel criado:", imovel._titulo)
    print("Amenidades:", len(imovel._amenidades))
    print("Fotos:", len(imovel._fotos))
    print("Avaliações:", len(imovel._avaliacoes))


def testar_anuncio_contrato_pagamento():
    print("\n== Teste Anúncio / Contrato / Pagamento ==")

    serv_anuncio = ServicoAnuncio()
    serv_contrato = ServicoContrato()
    serv_pagamento = ServicoPagamento()

    imovel = Imovel(
        endereco="Rua Marechal Deodoro, 50",
        status="Disponível",
        id_imovel=2,
        titulo="Casa Jardim",
        descricao="2 quartos",
        tipo="Casa",
        area_m2=80,
        valor_aluguel=2500
    )

    anuncio = serv_anuncio.criar_anuncio(
        id_anuncio=10,
        data_publicacao="15/11/2025",
        preco=2500,
        disponibilidade=True,
        imovel=imovel
    )

    locatario = Locatario("Nicole", "Bet", "Bet.nicole@mail.com",
                          "03/05/2005", "5148", 3, "12/10/2024",
                          "Pet friendly")

    contrato = serv_contrato.criar_contrato(
        numero_contrato=50,
        inicio="01/12/2025",
        fim="01/12/2026",
        valor_final=30000,
        anuncio=anuncio,
        locatario=locatario
    )

    pagamento = serv_pagamento.registrar_pagamento(
        id_pagamento=1,
        data_pagamento="05/12/2025",
        valor_pago=2500,
        metodo_pagamento="Pix"
    )

    contrato.adicionar_pagamento(pagamento)

    print("Anúncio criado:", anuncio._id_anuncio)
    print("Contrato número:", contrato._numero_contrato)
    print("Pagamentos registrados:", len(contrato._pagamentos))


if __name__ == "__main__":
    testar_locador_locatario()
    testar_imovel()
    testar_anuncio_contrato_pagamento()
    print("\n== Todos os testes executados ==")


