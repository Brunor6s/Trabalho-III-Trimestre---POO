import tkinter as tk
from tkinter import ttk, messagebox
from services import (
    criar_locador, criar_locatario, criar_imovel, listar_locadores,
    listar_locatarios, listar_anuncios_disponiveis, listar_imoveis,
    alugar_imovel, listar_contratos
)
from datetime import datetime

# -------------------- JANELAS DE CADASTRO --------------------

def abrir_cadastrar_locador(parent):
    w = tk.Toplevel(parent)
    w.title("Cadastrar Locador")

    labels = ["Primeiro nome", "Sobrenome", "Email", "Data nascimento (dd/mm/YYYY)", "Documento", "Conta bancária", "Avaliação (int)"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(w, text=text).grid(row=i, column=0, sticky="w", padx=6, pady=4)
        e = tk.Entry(w); e.grid(row=i, column=1, padx=6, pady=4)
        entries.append(e)

    def salvar():
        try:
            loc = criar_locador(
                primeiro_nome=entries[0].get(),
                sobrenome=entries[1].get(),
                email=entries[2].get(),
                data_nascimento=entries[3].get(),
                documento=entries[4].get(),
                conta_bancaria=entries[5].get(),
                avaliacao_proprietario=int(entries[6].get() or 0)
            )
            messagebox.showinfo("Sucesso", f"Locador cadastrado (ID {loc._id_pessoa})")
            w.destroy()
            atualizar_comboboxes()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar locador: {e}")

    tk.Button(w, text="Salvar", command=salvar).grid(row=len(labels), column=0, columnspan=2, pady=8)


def abrir_cadastrar_locatario(parent):
    w = tk.Toplevel(parent)
    w.title("Cadastrar Locatário")

    labels = ["Primeiro nome", "Sobrenome", "Email", "Data nascimento (dd/mm/YYYY)", "Documento", "Preferências"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(w, text=text).grid(row=i, column=0, sticky="w", padx=6, pady=4)
        e = tk.Entry(w); e.grid(row=i, column=1, padx=6, pady=4)
        entries.append(e)

    def salvar():
        try:
            loc = criar_locatario(
                primeiro_nome=entries[0].get(),
                sobrenome=entries[1].get(),
                email=entries[2].get(),
                data_nascimento=entries[3].get(),
                documento=entries[4].get(),
                preferencias=entries[5].get()
            )
            messagebox.showinfo("Sucesso", f"Locatário cadastrado (ID {loc._id_pessoa})")
            w.destroy()
            atualizar_comboboxes()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar locatário: {e}")

    tk.Button(w, text="Salvar", command=salvar).grid(row=len(labels), column=0, columnspan=2, pady=8)


def abrir_cadastrar_imovel(parent):
    w = tk.Toplevel(parent)
    w.title("Cadastrar Imóvel")

    labels = ["Endereço", "Status (Disponível)", "Título", "Descrição", "Tipo", "Área (m2)", "Valor aluguel (num)"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(w, text=text).grid(row=i, column=0, sticky="w", padx=6, pady=4)
        e = tk.Entry(w); e.grid(row=i, column=1, padx=6, pady=4)
        entries.append(e)

    tk.Label(w, text="Locador (ID)").grid(row=len(labels), column=0, sticky="w", padx=6, pady=4)
    combo_locador = ttk.Combobox(w, state="readonly")
    combo_locador.grid(row=len(labels), column=1, padx=6, pady=4)

    def preencher_locadores():
        vals = [f"{l._id_pessoa} - {l._primeiro_nome} {l._sobrenome}" for l in listar_locadores()]
        combo_locador['values'] = vals
        if vals:
            combo_locador.current(0)
    preencher_locadores()

    def salvar():
        try:
            loc_text = combo_locador.get()
            if not loc_text:
                raise ValueError("Selecione um locador")
            loc_id = int(loc_text.split(" - ")[0])
            imv = criar_imovel(
                endereco=entries[0].get(),
                status=entries[1].get() or "Disponível",
                titulo=entries[2].get(),
                descricao=entries[3].get(),
                tipo=entries[4].get(),
                area_m2=float(entries[5].get() or 0),
                valor_aluguel=float(entries[6].get() or 0),
                locador_id=loc_id
            )
            messagebox.showinfo("Sucesso", f"Imóvel cadastrado (ID {imv._id_imovel})")
            w.destroy()
            atualizar_comboboxes()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar imóvel: {e}")

    tk.Button(w, text="Salvar", command=salvar).grid(row=len(labels)+1, column=0, columnspan=2, pady=8)


# -------------------- LISTAGENS E ALUGUEL --------------------

def abrir_listagens(parent):
    w = tk.Toplevel(parent)
    w.title("Listagens")

    nb = ttk.Notebook(w); nb.pack(fill="both", expand=True, padx=6, pady=6)

    # LOCADORES
    f1 = tk.Frame(nb)
    txt1 = tk.Text(f1, width=80, height=20)
    txt1.pack(fill="both", expand=True)
    texto = ""
    for l in listar_locadores():
        texto += f"Locador ID {l._id_pessoa}: {l._primeiro_nome} {l._sobrenome} | Email: {l._email}\n"
        if getattr(l, "_imoveis", None):
            for im in l._imoveis:
                texto += f"   → Imóvel ID {im._id_imovel}: {im._titulo} | {im._endereco} | Status: {im._status}\n"
    txt1.insert("1.0", texto or "Nenhum locador cadastrado.")
    nb.add(f1, text="Locadores")

    # LOCATÁRIOS
    f2 = tk.Frame(nb)
    txt2 = tk.Text(f2, width=80, height=20)
    txt2.pack(fill="both", expand=True)
    texto = ""
    for l in listar_locatarios():
        texto += f"Locatário ID {l._id_pessoa}: {l._primeiro_nome} {l._sobrenome} | Email: {l._email}\n"
    txt2.insert("1.0", texto or "Nenhum locatário cadastrado.")
    nb.add(f2, text="Locatários")

    # IMÓVEIS
    f3 = tk.Frame(nb)
    txt3 = tk.Text(f3, width=80, height=20)
    txt3.pack(fill="both", expand=True)
    texto = ""
    for im in listar_imoveis():
        texto += f"Imóvel ID {im._id_imovel}: {im._titulo} | {im._endereco} | Status: {im._status} | Valor: {im._valor_aluguel}\n"
    txt3.insert("1.0", texto or "Nenhum imóvel cadastrado.")
    nb.add(f3, text="Imóveis")

    # CONTRATOS
    f4 = tk.Frame(nb)
    txt4 = tk.Text(f4, width=80, height=20)
    txt4.pack(fill="both", expand=True)
    texto = ""
    for c in listar_contratos():
        texto += f"Contrato Nº {c._numero_contrato}: Imóvel '{c._anuncio._imovel._titulo}' | Locatário: {c._locatario._primeiro_nome} {c._locatario._sobrenome} | {c._data_inicio} → {c._data_fim} | Valor: {c._valor_final}\n"
    txt4.insert("1.0", texto or "Nenhum contrato registrado.")
    nb.add(f4, text="Contratos")


def abrir_alugar(parent):
    w = tk.Toplevel(parent)
    w.title("Alugar Imóvel")

    tk.Label(w, text="Anúncio disponível:").grid(row=0, column=0, sticky="w", padx=6, pady=4)
    cb_anuncios = ttk.Combobox(w, state="readonly", width=60)
    cb_anuncios.grid(row=0, column=1, padx=6, pady=4)

    tk.Label(w, text="Locatário:").grid(row=1, column=0, sticky="w", padx=6, pady=4)
    cb_locatarios = ttk.Combobox(w, state="readonly", width=60)
    cb_locatarios.grid(row=1, column=1, padx=6, pady=4)

    tk.Label(w, text="Data início (dd/mm/YYYY):").grid(row=2, column=0, sticky="w", padx=6, pady=4)
    e_inicio = tk.Entry(w); e_inicio.grid(row=2, column=1, padx=6, pady=4)
    e_inicio.insert(0, datetime.now().strftime("%d/%m/%Y"))

    tk.Label(w, text="Data fim (dd/mm/YYYY):").grid(row=3, column=0, sticky="w", padx=6, pady=4)
    e_fim = tk.Entry(w); e_fim.grid(row=3, column=1, padx=6, pady=4)
    e_fim.insert(0, datetime.now().strftime("%d/%m/%Y"))

    def preencher():
        anuncios = listar_anuncios_disponiveis()
        anuncios_str = [f"{a._id_anuncio} - {a._imovel._titulo} ({a._imovel._endereco}) - R$ {a._preco}" for a in anuncios]
        cb_anuncios['values'] = anuncios_str
        if anuncios_str:
            cb_anuncios.current(0)

        locs = listar_locatarios()
        locs_str = [f"{l._id_pessoa} - {l._primeiro_nome} {l._sobrenome}" for l in locs]
        cb_locatarios['values'] = locs_str
        if locs_str:
            cb_locatarios.current(0)

    preencher()

    def confirmar_aluguel():
        try:
            an = cb_anuncios.get()
            if not an:
                raise ValueError("Selecione um anúncio")
            anuncio_id = int(an.split(" - ")[0])
            loc = cb_locatarios.get()
            if not loc:
                raise ValueError("Selecione um locatário")
            loc_id = int(loc.split(" - ")[0])
            contrato = alugar_imovel(anuncio_id, loc_id, e_inicio.get(), e_fim.get())
            messagebox.showinfo("Sucesso", f"Contrato criado: Nº {contrato._numero_contrato}")
            w.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao alugar: {e}")
        finally:
            atualizar_comboboxes()

    tk.Button(w, text="Confirmar aluguel", command=confirmar_aluguel).grid(row=4, column=0, columnspan=2, pady=10)


# -------------------- UTIL / MAIN --------------------

def atualizar_comboboxes():
    # placeholder: as comboboxes são preenchidas quando as janelas abrem
    pass


def main():
    root = tk.Tk()
    root.title("Sistema de Locação - Tkinter (Memória)")
    root.geometry("520x360")

    tk.Label(root, text="Sistema de Locação", font=("Helvetica", 16)).pack(pady=12)

    frame = tk.Frame(root)
    frame.pack(pady=8)

    tk.Button(frame, text="Cadastrar Locador", width=30, command=lambda: abrir_cadastrar_locador(root)).grid(row=0, column=0, pady=6)
    tk.Button(frame, text="Cadastrar Locatário", width=30, command=lambda: abrir_cadastrar_locatario(root)).grid(row=1, column=0, pady=6)
    tk.Button(frame, text="Cadastrar Imóvel", width=30, command=lambda: abrir_cadastrar_imovel(root)).grid(row=2, column=0, pady=6)
    tk.Button(frame, text="Listagens", width=30, command=lambda: abrir_listagens(root)).grid(row=3, column=0, pady=6)
    tk.Button(frame, text="Alugar Imóvel", width=30, command=lambda: abrir_alugar(root)).grid(row=4, column=0, pady=6)

    tk.Label(root, text="Observação: o sistema salva apenas na memória (execução atual).").pack(side="bottom", pady=8)

    root.mainloop()


if __name__ == "__main__":
    main()