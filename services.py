from datetime import datetime
from classes import (
    Locador, Locatario, Imovel, Amenidade, Anuncio, Contrato, Avaliacao, Pagamento
)

# "Banco" em memória
bd = {
    "locadores": [],
    "locatarios": [],
    "imoveis": [],
    "anuncios": [],
    "contratos": []
}

# Contadores simples para gerar IDs
counters = {
    "pessoa_id": 1,
    "imovel_id": 1,
    "anuncio_id": 1,
    "contrato_num": 1,
    "avaliacao_id": 1,
    "pagamento_id": 1
}


# ---------------------- CRUD / Creation ----------------------

def criar_locador(primeiro_nome, sobrenome, email, data_nascimento, documento,
                  conta_bancaria="", avaliacao_proprietario=0):
    pid = counters["pessoa_id"]; counters["pessoa_id"] += 1
    data_cadastro = datetime.now().strftime("%d/%m/%Y")
    loc = Locador(
        primeiro_nome=primeiro_nome,
        sobrenome=sobrenome,
        email=email,
        data_nascimento=data_nascimento,
        documento=documento,
        id_pessoa=pid,
        data_cadastro=data_cadastro,
        conta_bancaria=conta_bancaria,
        avaliacao_proprietario=avaliacao_proprietario
    )
    bd["locadores"].append(loc)
    return loc


def criar_locatario(primeiro_nome, sobrenome, email, data_nascimento, documento, preferencias=""):
    pid = counters["pessoa_id"]; counters["pessoa_id"] += 1
    data_cadastro = datetime.now().strftime("%d/%m/%Y")
    loc = Locatario(
        primeiro_nome=primeiro_nome,
        sobrenome=sobrenome,
        email=email,
        data_nascimento=data_nascimento,
        documento=documento,
        id_pessoa=pid,
        data_cadastro=data_cadastro,
        preferencias=preferencias
    )
    bd["locatarios"].append(loc)
    return loc


def criar_imovel(endereco, status, titulo, descricao, tipo, area_m2, valor_aluguel, locador_id):
    iid = counters["imovel_id"]; counters["imovel_id"] += 1
    imv = Imovel(
        endereco=endereco,
        status=status,
        id_imovel=iid,
        titulo=titulo,
        descricao=descricao,
        tipo=tipo,
        area_m2=area_m2,
        valor_aluguel=valor_aluguel
    )
    # associar ao locador
    loc = buscar_locador_por_id(locador_id)
    if loc is None:
        raise ValueError("Locador não encontrado")
    loc.adicionar_imovel(imv)
    bd["imoveis"].append(imv)
    # criar anúncio automático
    criar_anuncio_para_imovel(imv, preco=valor_aluguel)
    return imv


def criar_anuncio_para_imovel(imovel, preco):
    aid = counters["anuncio_id"]; counters["anuncio_id"] += 1
    anuncio = Anuncio(
        id_anuncio=aid,
        data_publicacao=datetime.now().strftime("%d/%m/%Y"),
        preco=preco,
        disponibilidade=True,
        imovel=imovel
    )
    bd["anuncios"].append(anuncio)
    # vincular ao imóvel
    imovel.adicionar_anuncio(anuncio)
    return anuncio


# ---------------------- BUSCAS SIMPLES ----------------------

def listar_locadores():
    return bd["locadores"]


def listar_locatarios():
    return bd["locatarios"]


def listar_imoveis(disponiveis_only=False):
    if not disponiveis_only:
        return bd["imoveis"]
    return [i for i in bd["imoveis"] if i._status.lower() in ("disponível", "disponivel", "disponivel".lower()) or any(
        (hasattr(a, "_disponibilidade") and a._disponibilidade) for a in getattr(i, "_anuncios", [])
    )]


def listar_anuncios_disponiveis():
    return [a for a in bd["anuncios"] if getattr(a, "_disponibilidade", False)]


def buscar_locador_por_id(id_pessoa):
    for l in bd["locadores"]:
        if getattr(l, "_id_pessoa", None) == id_pessoa:
            return l
    return None


def buscar_locatario_por_id(id_pessoa):
    for l in bd["locatarios"]:
        if getattr(l, "_id_pessoa", None) == id_pessoa:
            return l
    return None


def buscar_imovel_por_id(id_imovel):
    for i in bd["imoveis"]:
        if getattr(i, "_id_imovel", None) == id_imovel:
            return i
    return None


def buscar_anuncio_por_id(id_anuncio):
    for a in bd["anuncios"]:
        if getattr(a, "_id_anuncio", None) == id_anuncio:
            return a
    return None


# ---------------------- FLUXO DE ALUGUEL ----------------------

def alugar_imovel(anuncio_id, locatario_id, data_inicio_str, data_fim_str):
    anuncio = buscar_anuncio_por_id(anuncio_id)
    if anuncio is None:
        raise ValueError("Anúncio não encontrado")
    if not getattr(anuncio, "_disponibilidade", False):
        raise ValueError("Anúncio não disponível")

    locatario = buscar_locatario_por_id(locatario_id)
    if locatario is None:
        raise ValueError("Locatário não encontrado")

    imovel = getattr(anuncio, "_imovel", None)
    if imovel is None:
        raise ValueError("Imóvel do anúncio inválido")

    # criar contrato
    numero = counters["contrato_num"]; counters["contrato_num"] += 1
    # calcular valor final simplificado: diária * dias (aqui usamos preco do anúncio * 1 para simplicidade)
    try:
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
        dias = max(1, (data_fim - data_inicio).days)
    except Exception:
        dias = 1
    valor_final = getattr(anuncio, "_preco", 0) * dias

    contrato = Contrato(
        numero_contrato=numero,
        data_inicio=data_inicio_str,
        data_fim=data_fim_str,
        valor_final=valor_final,
        anuncio=anuncio,
        locatario=locatario
    )
    bd["contratos"].append(contrato)

    # atualizar disponibilidade do anúncio e status do imóvel
    anuncio._disponibilidade = False
    imovel._status = "Alugado"

    return contrato


# ---------------------- AUXILIARES ----------------------

def remover_anuncio(anuncio_id):
    a = buscar_anuncio_por_id(anuncio_id)
    if a:
        bd["anuncios"].remove(a)
        im = getattr(a, "_imovel", None)
        if im and a in getattr(im, "_anuncios", []):
            im._anuncios.remove(a)
        return True
    return False


def listar_contratos():
    return bd["contratos"]