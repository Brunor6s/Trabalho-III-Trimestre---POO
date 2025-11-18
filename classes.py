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

