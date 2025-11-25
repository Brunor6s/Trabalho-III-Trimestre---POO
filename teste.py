from classes import (
    Locador, Locatario, Telefone, Foto, Amenidade, Avaliacao,
    Imovel, Anuncio, Contrato, Pagamento
)


def testar_locador_locatario():
    print("== Teste Pessoa / Locador / Locatário ==")

    locador = Locador(
        "Maria", "Jobim", "maria@email.com",
        "10/01/1985", "123456789", 1,
        "18/11/2024", "Banco XP", 5
    )

    locatario = Locatario(
        "Jordan", "Kuhn", "jordan@email.com",
        "03/03/2007", "987654321", 2,
        "10/10/2024", "Silencioso"
    )

    tel = Telefone("99999-0000")
    locador.adicionar_telefone(tel)

    print(locador.exibir_informacoes())
    print(locatario.exibir_informacoes())
    print("Telefone do locador adicionado:", locador._telefones[0]._numero)


def testar_imovel():
    print("\n== Teste Imóvel ==")

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

    foto = Foto("fotos/img1.jpg")
    amenidade = Amenidade(1, "Piscina")
    avaliacao = Avaliacao(1, 5, "Ótimo lugar", "12/12/2024")

    imovel.adicionar_foto(foto)
    imovel.adicionar_amenidade(amenidade)
    imovel.adicionar_avaliacao(avaliacao)

    print("Título:", imovel._titulo)
    print("Fotos:", len(imovel._fotos))
    print("Amenidades:", len(imovel._amenidades))
    print("Avaliações:", len(imovel._avaliacoes))


def testar_anuncio_contrato_pagamento():
    print("\n== Teste Anúncio / Contrato / Pagamento ==")

    imovel = Imovel(
        endereco="Rua Marechal Deodoro",
        status="Disponível",
        id_imovel=10,
        titulo="Casa Grande",
        descricao="2 quartos",
        tipo="Casa",
        area_m2=80,
        valor_aluguel=2500
    )

    anuncio = Anuncio(
        id_anuncio=100,
        data_publicacao="18/11/2025",
        preco=2500,
        disponibilidade=True,
        imovel=imovel
    )

    locatario = Locatario(
        "Nicole", "Bet", "nicole@email.com",
        "03/05/2005", "5148", 3,
        "12/10/2024", "Pet friendly"
    )

    contrato = Contrato(
        numero_contrato=50,
        data_inicio="01/12/2025",
        data_fim="01/12/2026",
        valor_final=30000,
        anuncio=anuncio,
        locatario=locatario
    )

    pagamento = Pagamento(
        id_pagamento=1,
        data_pagamento="10/12/2025",
        valor_pago=2500,
        metodo_pagamento="Pix"
    )

    contrato.adicionar_pagamento(pagamento)

    print("Anúncio ID:", anuncio._id_anuncio)
    print("Contrato:", contrato._numero_contrato)
    print("Pagamentos:", len(contrato._pagamentos))


if __name__ == "__main__":
    testar_locador_locatario()
    testar_imovel()
    testar_anuncio_contrato_pagamento()
    print("\n== Testes finalizados ==")