import tkinter as tk
from tkinter import messagebox
from datetime import date

from classes import Cliente, Funcionario, Quarto
from services import ClienteService, FuncionarioService, QuartoService, ReservaService

def parse_data(txt):
    try:
        y, m, d = map(int, txt.split("-"))
        return date(y, m, d)
    except:
        messagebox.showerror("Erro", "Data inválida! Use AAAA-MM-DD")
        return None

class InterfaceHotel:
    def __init__(self):
        self.clienteService = ClienteService()
        self.funcService = FuncionarioService()
        self.quartoService = QuartoService()
        self.reservaService = ReservaService()

        self.tipo_logado = None

        self.cliente_padrao = Cliente("Rogério", "123", "rogerio@gmail.com", 1, "1234-5678")
        self.func_padrao = Funcionario("Peter", "123", "peter@hotel.com", 1, "Recepção")
        self.clienteService.cadastrarCliente(self.cliente_padrao)
        self.funcService.cadastrarFuncionario(self.func_padrao)

        self.quartoService.adicionarQuarto(Quarto(101, "Solteiro", 150))
        self.quartoService.adicionarQuarto(Quarto(102, "Casal", 200))

        self.janela = tk.Tk()
        self.janela.title("Sistema de Hotel")

        tk.Label(self.janela, text="Login (c = cliente / f = funcionário / d = dono)").pack()
        self.usuario = tk.Entry(self.janela)
        self.usuario.pack()

        tk.Label(self.janela, text="Senha").pack()
        self.senha = tk.Entry(self.janela, show="*")
        self.senha.pack()

        tk.Button(self.janela, text="Entrar", command=self.login).pack(pady=10)
        self.janela.mainloop()

    def limpar(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def login(self):
        u = self.usuario.get()
        s = self.senha.get()

        usuarios = {
            "c": {"senha": "123", "tipo": "cliente"},
            "f": {"senha": "123", "tipo": "funcionario"},
            "d": {"senha": "123", "tipo": "dono"},
        }

        if u not in usuarios or usuarios[u]["senha"] != s:
            messagebox.showerror("Erro", "Login inválido!")
            return

        self.tipo_logado = usuarios[u]["tipo"]
        self.limpar()

        if self.tipo_logado == "cliente":
            self.menu_cliente()
        elif self.tipo_logado == "funcionario":
            self.menu_func()
        else:
            self.menu_dono()

    def menu_cliente(self):
        tk.Label(self.janela, text="Menu Cliente").pack()
        tk.Button(self.janela, text="Quartos Disponíveis", command=self.ver_quartos).pack(pady=4)
        tk.Button(self.janela, text="Fazer Reserva", command=self.fazer_reserva).pack(pady=4)
        tk.Button(self.janela, text="Minhas Reservas", command=self.minhas_reservas).pack(pady=4)
        tk.Button(self.janela, text="Logout", command=self.resetar).pack(pady=4)

    def ver_quartos(self):
        quartos = self.quartoService.listarQuartos()
        texto = ""
        for q in quartos:
            status = "Livre" if q.disponivel else "Ocupado"
            texto += f"Quarto {q.numero} - {q.tipo} - R$ {q.precoDiaria:.2f} - {status}\n"
        if texto == "":
            texto = "Nenhum quarto cadastrado."
        messagebox.showinfo("Quartos Disponíveis", texto)

    def fazer_reserva(self):
        self.limpar()
        tk.Label(self.janela, text="Check-in (AAAA-MM-DD)").pack()
        ent1 = tk.Entry(self.janela); ent1.pack()
        tk.Label(self.janela, text="Check-out (AAAA-MM-DD)").pack()
        ent2 = tk.Entry(self.janela); ent2.pack()

        def confirmar():
            d1 = parse_data(ent1.get())
            d2 = parse_data(ent2.get())
            if not d1 or not d2:
                return

            quarto = self.quartoService.buscarDisponivel()
            if not quarto:
                messagebox.showwarning("Aviso", "Nenhum quarto disponível!")
                return

            reserva = self.reservaService.criarReserva(
                idReserva=len(self.reservaService.reservas)+1,
                dataEntrada=d1,
                dataSaida=d2,
                cliente=self.cliente_padrao,
                quarto=quarto
            )

            total = reserva.calcularTotal()
            messagebox.showinfo("Reserva", f"Reserva criada! Valor total: R$ {total:.2f}")
            self.menu_cliente()

        tk.Button(self.janela, text="Confirmar", command=confirmar).pack(pady=5)
        tk.Button(self.janela, text="Voltar", command=self.menu_cliente).pack()

    def minhas_reservas(self):
        texto = ""
        for r in self.reservaService.reservas:
            if r.cliente.nome == self.cliente_padrao.nome:
                texto += f"Reserva {r.idReserva} - Quarto {r.quarto.numero}\n"
        if texto == "":
            texto = "Nenhuma reserva encontrada."
        messagebox.showinfo("Minhas Reservas", texto)

    def menu_func(self):
        tk.Label(self.janela, text="Menu Funcionário").pack()
        tk.Button(self.janela, text="Listar Reservas", command=self.listar_reservas).pack(pady=4)
        tk.Button(self.janela, text="Listar Quartos", command=self.listar_quartos).pack(pady=4)
        tk.Button(self.janela, text="Logout", command=self.resetar).pack(pady=4)

    def listar_reservas(self):
        texto = ""
        for r in self.reservaService.listarReservas():
            texto += f"Reserva {r.idReserva}: Quarto {r.quarto.numero} - Cliente {r.cliente.nome} - {r.dataCheckin} a {r.dataCheckout}\n"
        if texto == "":
            texto = "Nenhuma reserva cadastrada."
        messagebox.showinfo("Reservas", texto)

    def listar_quartos(self):
        texto = ""
        for q in self.quartoService.listarQuartos():
            status = "Livre" if q.disponivel else "Ocupado"
            texto += f"Quarto {q.numero} - {q.tipo} - R$ {q.precoDiaria:.2f} - {status}\n"
        if texto == "":
            texto = "Nenhum quarto cadastrado."
        messagebox.showinfo("Quartos", texto)

    def menu_dono(self):
        tk.Label(self.janela, text="Menu Dono").pack()
        tk.Button(self.janela, text="Cadastrar Funcionário", command=self.cadastrar_funcionario).pack(pady=4)
        tk.Button(self.janela, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack(pady=4)
        tk.Button(self.janela, text="Listar Funcionários", command=self.listar_funcionarios).pack(pady=4)
        tk.Button(self.janela, text="Listar Quartos", command=self.listar_quartos).pack(pady=4)
        tk.Button(self.janela, text="Logout", command=self.resetar).pack(pady=4)

    def listar_funcionarios(self):
        texto = ""
        for f in self.funcService.listarFuncionarios():
            texto += f"{f.idFuncionario} - {f.nome} - {f.cargo}\n"
        if texto == "":
            texto = "Nenhum funcionário cadastrado."
        messagebox.showinfo("Funcionários", texto)

    def cadastrar_cliente(self):
        self.limpar()
        tk.Label(self.janela, text="Nome do Cliente").pack()
        nome = tk.Entry(self.janela); nome.pack()
        tk.Label(self.janela, text="Email").pack()
        email = tk.Entry(self.janela); email.pack()

        def salvar():
            novo = Cliente(nome.get(), "123", email.get(), len(self.clienteService.clientes)+1, "0000")
            self.clienteService.cadastrarCliente(novo)
            messagebox.showinfo("OK", "Cliente cadastrado!")
            self.menu_dono()

        tk.Button(self.janela, text="Salvar", command=salvar).pack()
        tk.Button(self.janela, text="Voltar", command=self.menu_dono).pack()

    def cadastrar_funcionario(self):
        self.limpar()
        tk.Label(self.janela, text="Nome do Funcionário").pack()
        nome = tk.Entry(self.janela); nome.pack()
        tk.Label(self.janela, text="Cargo").pack()
        cargo = tk.Entry(self.janela); cargo.pack()

        def salvar():
            novo = Funcionario(nome.get(), "123", f"{nome.get()}@email.com", len(self.funcService.funcionarios)+1, cargo.get())
            self.funcService.cadastrarFuncionario(novo)
            messagebox.showinfo("OK", "Funcionário cadastrado!")
            self.menu_dono()

        tk.Button(self.janela, text="Salvar", command=salvar).pack()
        tk.Button(self.janela, text="Voltar", command=self.menu_dono).pack()

    def resetar(self):
        self.limpar()
        self.__init__()

if __name__ == "__main__":
    InterfaceHotel()
