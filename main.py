## main.py

python
from datetime import date, timedelta
from classes import Proprietario, Locatario, Endereco, Imovel
from services import ContratoService, DescontoService
from repository import ImovelRepository

repo = ImovelRepository()


prop = Proprietario('Ana Silva', 'ana@example.com', '123.456.789-00')
end = Endereco('Rua A', '10', 'São Paulo', 'SP')
imovel = Imovel('Apê Centro', 'Apartamento 1 quarto', end, 2000.0)
prop.adicionar_imovel(imovel)
repo.adicionar(imovel)


loc = Locatario('João Pereira', 'joao@example.com', 'MG-12.345.678')

cs = ContratoService()
inicio = date.today()
fim = inicio.replace(year=inicio.year + 1)
contrato = cs.criar_contrato(imovel, prop, loc, inicio, fim)

print(f"Contrato criado entre {prop.nome} e {loc.nome}, duração {contrato.duracao_dias} dias")


ds = DescontoService()
total = ds.calcular_total(imovel, 12, loc)
print(f"Total para 12 meses com desconto: R$ {total:.2f}")


print('Imóveis disponíveis:', [i.titulo for i in repo.listar_disponiveis()])


contrato.cancelar()
print('Contrato ativo?', contrato.esta_ativo())
print('Imóveis disponíveis depois do cancelamento:', [i.titulo for i in repo.listar_disponiveis()])

