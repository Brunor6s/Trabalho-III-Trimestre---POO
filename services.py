from classes import (
    Pessoa, Locador, Locatario, Imovel, Amenidade,
    Avaliacao, Pagamento, Anuncio, Contrato
)


#Entidades
def criar_pessoa(nome, email, documento, data_nascimento):
    return Pessoa(nome, email, documento, data_nascimento)


def criar_locador(nome, email, documento, data_nascimento, conta_bancaria):
    return Locador(nome, email, documento, data_nascimento, conta_bancaria)


def criar_locatario(nome, email, documento, data_nascimento, preferencias=None):
    return Locatario(nome, email, documento, data_nascimento, preferencias)


def criar_imovel(titulo, descricao, endereco, preco_base, locador):
    return Imovel(titulo, descricao, endereco, preco_base, locador)


def criar_amenidade(nome, descricao):
    return Amenidade(nome, descricao)


def criar_anuncio(imovel, titulo, descricao, preco_dia):
    return Anuncio(imovel, titulo, descricao, preco_dia)


def criar_avaliacao(nota, comentario, autor, imovel):
    return Avaliacao(nota, comentario, autor, imovel)


def criar_pagamento(valor, metodo, status):
    return Pagamento(valor, metodo, status)


def criar_contrato(imovel, locatario, data_inicio, data_fim, valor_total):
    return Contrato(imovel, locatario, data_inicio, data_fim, valor_total)


#Relacionamento
def adicionar_amenidade_ao_imovel(imovel, amenidade):
    imovel.adicionar_amenidade(amenidade)


def adicionar_foto_ao_imovel(imovel, foto):
    imovel.adicionar_foto(foto)


def adicionar_avaliacao_ao_imovel(imovel, avaliacao):
    imovel.adicionar_avaliacao(avaliacao)


def adicionar_anuncio_ao_imovel(imovel, anuncio):
    imovel.adicionar_anuncio(anuncio)


def registrar_pagamento_em_contrato(contrato, pagamento):
    contrato.adicionar_pagamento(pagamento)