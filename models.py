from abc import ABC, abstractmethod




class Endereco:
# composição: Endereco faz sentido existir apenas dentro do Imovel
def __init__(self, rua: str, numero: str, cidade: str, estado: str):
self.rua = rua
self.numero = numero
self.cidade = cidade
self.estado = estado


def __str__(self):
return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"




class Imovel:
def __init__(self, titulo: str, descricao: str, endereco: Endereco, aluguel_mensal: float):
self._titulo = titulo
self._descricao = descricao
self._endereco = endereco # composição
self._aluguel_mensal = aluguel_mensal
self._disponivel = True


@property
def titulo(self) -> str:
return self._titulo


@property
def aluguel_mensal(self) -> float:
return self._aluguel_mensal


@property
def disponivel(self) -> bool:
return self._disponivel


def marcar_indisponivel(self):
self._disponivel = False


def marcar_disponivel(self):
self._disponivel = True




class Contrato:
def __init__(self, imovel: Imovel, proprietario: Proprietario, locatario: Locatario, data_inicio: date, data_fim: date):
if data_fim <= data_inicio:
raise ValueError('data_fim deve ser posterior a data_inicio')
if not imovel.disponivel:
raise ValueError('Imóvel não está disponível')
self._imovel = imovel # associação
self._proprietario = proprietario
self._locatario = locatario
self._data_inicio = data_inicio
self._data_fim = data_fim
self._ativo = True
# composição: contrato possui as regras de pagamento/parcelas — aqui apenas conceito
imovel.marcar_indisponivel()


@property
def duracao_dias(self) -> int:
return (self._data_fim - self._data_inicio).days


def cancelar(self):
if not self._ativo:
return
self._ativo = False
self._imovel.marcar_disponivel()


def esta_ativo(self) -> bool:
return self._ativo