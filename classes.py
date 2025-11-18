from abc import ABC, abstractmethod

#Classe da Pessoa
class Pessoa(ABC):
    def __init__(self, primeiro_nome, sobrenome, email, data_nascimento,
                 documento, id_pessoa, data_cadastro):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._email = email
        self._data_nascimento = data_nascimento
        self._documento = documento
        self._id_pessoa = id_pessoa
        self._data_cadastro = data_cadastro
        self._telefones = []  

    @property
    def email(self):
        return self._email

    @abstractmethod
    def exibir_informacoes(self):
        pass

    def adicionar_telefone(self, telefone):
        self._telefones.append(telefone)

#Telefone
class Telefone:
    def __init__(self, numero):
        self._numero = numero

#Locador 
class Locador(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, email, data_nascimento,
                 documento, id_pessoa, data_cadastro, conta_bancaria,
                 avaliacao_proprietario):
        super().__init__(primeiro_nome, sobrenome, email, data_nascimento,
                         documento, id_pessoa, data_cadastro)

        self._conta_bancaria = conta_bancaria
        self._avaliacao_proprietario = avaliacao_proprietario
        self._imoveis = []  # relação 1,n

    def adicionar_imovel(self, imovel):
        self._imoveis.append(imovel)

    def exibir_informacoes(self):
        return f"Locador: {self._primeiro_nome} {self._sobrenome}"

#Locatorio
class Locatario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, email, data_nascimento,
                 documento, id_pessoa, data_cadastro, preferencias):
        super().__init__(primeiro_nome, sobrenome, email, data_nascimento,
                         documento, id_pessoa, data_cadastro)

        self._preferencias = preferencias

    def exibir_informacoes(self):
        return f"Locatário: {self._primeiro_nome} {self._sobrenome}"

#Foto
class Foto:
    def __init__(self, caminho):
        self._caminho = caminho

#Amenidade
class Amenidade:
    def __init__(self, id_amenidade, nome):
        self._id_amenidade = id_amenidade
        self._nome = nome

#Avaliação
class Avaliacao:
    def __init__(self, id_avaliacao, nota, comentario, data):
        self._id_avaliacao = id_avaliacao
        self._nota = nota
        self._comentario = comentario
        self._data = data

#Imóvel
class Imovel:
    def __init__(self, endereco, status, id_imovel, titulo,
                 descricao, tipo, area_m2, valor_aluguel):
        self._endereco = endereco
        self._status = status
        self._id_imovel = id_imovel
        self._titulo = titulo
        self._descricao = descricao
        self._tipo = tipo
        self._area_m2 = area_m2
        self._valor_aluguel = valor_aluguel

        self._fotos = []        
        self._amenidades = []   
        self._avaliacoes = []   
        self._anuncios = []     
    def adicionar_foto(self, foto):
        self._fotos.append(foto)

    def adicionar_amenidade(self, amenidade):
        self._amenidades.append(amenidade)

    def adicionar_avaliacao(self, avaliacao):
        self._avaliacoes.append(avaliacao)

    def adicionar_anuncio(self, anuncio):
        self._anuncios.append(anuncio)

#Anúncio
class Anuncio:
    def __init__(self, id_anuncio, data_publicacao, preco, disponibilidade, imovel):
        self._id_anuncio = id_anuncio
        self._data_publicacao = data_publicacao
        self._preco = preco
        self._disponibilidade = disponibilidade
        self._imovel = imovel

#Contrato 
class Contrato:
    def __init__(self, numero_contrato, data_inicio, data_fim, valor_final, anuncio, locatario):
        self._numero_contrato = numero_contrato
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._valor_final = valor_final
        self._anuncio = anuncio
        self._locatario = locatario
        self._pagamentos = [] 

    def adicionar_pagamento(self, pagamento):
        self._pagamentos.append(pagamento)

#Pagamentos
class Pagamento:
    def __init__(self, id_pagamento, data_pagamento, valor_pago, metodo_pagamento):
        self._id_pagamento = id_pagamento
        self._data_pagamento = data_pagamento
        self._valor_pago = valor_pago
        self._metodo_pagamento = metodo_pagamento
