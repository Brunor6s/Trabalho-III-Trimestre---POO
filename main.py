# main.py
from datetime import date
from classes import Locador, Locatario, Imovel, Amenidade, Anuncio


#Objetos
locador = Locador(
    primeiro_nome="Maria",
    sobrenome="Emelau",
    email="emelau@gmail.com",
    data_nascimento="10/01/1985",
    documento="123.456.789-00",
    id_pessoa=1,
    data_cadastro="18/11/2024",
    conta_bancaria="NuBank - 1234",
    avaliacao_proprietario=5
)

locatario = Locatario(
    primeiro_nome="Rogerio",
    sobrenome="Ceni",
    email="r.ceni@example.com",
    data_nascimento="01/05/1990",
    documento="SP-12.345.678",
    id_pessoa=2,
    data_cadastro="18/11/2024",
    preferencias="Silencioso"
)


#Amenidades
g2porta = Amenidade(id_amenidade=1, nome="Geladeira duas portas")
ar = Amenidade(id_amenidade=2, nome="Ar-Condicionado")


# Criando imóvel
imovel = Imovel(
    endereco="Avenida Brasil, 100",
    status="Disponível",
    id_imovel=10,
    titulo="Apartamento Centro",
    descricao="1 quarto, sala, cozinha",
    tipo="Apartamento",
    area_m2=45,
    valor_aluguel=1800
)

# Relacionando amenidades
imovel.adicionar_amenidade(g2porta)
imovel.adicionar_amenidade(ar)

# Criando anúncio
anuncio = Anuncio(
    id_anuncio=100,
    data_publicacao="18/11/2025",
    preco=1800,
    disponibilidade=True,
    imovel=imovel
)


# Exibindo algumas informações
print("Locador:", locador.exibir_informacoes())
print("Locatário:", locatario.exibir_informacoes())
print("Imóvel:", imovel._titulo)
print("Amenidades:", [a._nome for a in imovel._amenidades])
print("Anúncio criado ID:", anuncio._id_anuncio)
