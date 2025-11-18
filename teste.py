
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

    locatario = Locatario("Jorda", "Kuhn", "jordan_kuhn@email.com",
                          "05/03/2007", "654321", 2, "11/11/2024",
                          "Silencioso")

    print(locador.exibir_informacoes())
    print(locatario.exibir_informacoes())

    tel = Telefone("98461-3853")
    locador.adicionar_telefone(tel)




