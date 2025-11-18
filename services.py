# servicos.py
# Serviços simples baseados SOMENTE no modelo lógico enviado

from modelos import (
    Pessoa, Locador, Locatario,
    Imovel, Avaliacao, Amenidade,
    Pagamento, Contrato, Anuncio, Prioridade
)


class ServicoPessoa:
    def criar_pessoa(self, nome, email, documento):
        return Pessoa(nome, email, documento)


class ServicoLocador:
    def criar_locador(self, pessoa):
        return Locador(pessoa)

    def adicionar_imovel(self, locador, imovel):
        locador.adicionar_imovel(imovel)


class ServicoLocatario:
    def criar_locatario(self, pessoa):
        return Locatario(pessoa)

    def favoritar_imovel(self, locatario, imovel, data):
        locatario.favoritar(imovel, data)


class ServicoImovel:
    def criar_imovel(self, id_imovel, titulo, descricao, tipo, area, valor):
        return Imovel(id_imovel, titulo, descricao, tipo, area, valor)

    def adicionar_amenidade(self, imovel, amenidade):
        imovel.adicionar_amenidade(amenidade)

    def adicionar_foto(self, imovel, foto):
        imovel.adicionar_foto(foto)

    def adicionar_avaliacao(self, imovel, avaliacao):
        imovel.adicionar_avaliacao(avaliacao)


class ServicoAvaliacao:
    def criar_avaliacao(self, nota, comentario, data):
        return Avaliacao(nota, comentario, data)


class ServicoAmenidade:
    def criar_amenidade(self, nome):
        return Amenidade(nome)


class ServicoPrioridade:
    def definir_prioridade(self, imovel, nivel):
        imovel.definir_prioridade(Prioridade(nivel))


class ServicoAnuncio:
    def criar_anuncio(self, imovel, preco, data_pub, disponibilidade):
        anuncio = Anuncio(imovel, preco, data_pub, disponibilidade)
        return anuncio


class ServicoContrato:
    def criar_contrato(self, numero, inicio, fim, valor_final, locatario, anuncio):
        return Contrato(numero, inicio, fim, valor_final, locatario, anuncio)


class ServicoPagamento:
    def registrar_pagamento(self, valor, data, metodo):
        return Pagamento(valor, data, metodo)
