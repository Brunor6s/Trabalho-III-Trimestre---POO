import tkinter as tk
from tkinter import messagebox
from classes import Cliente, Funcionario, Quarto
from services import ClienteService, FuncionarioService, QuartoService, ReservaService
from datetime import date

# Função auxiliar para converter datas simples
def parse_data(txt):
    try:
        y, m, d = map(int, txt.split("-"))
        return date(y, m, d)
    except:
        messagebox.showerror("Erro", "Data inválida, Use YYYY-MM-DD")
        return None

class InterfaceHotel:
    def __init__(self):
        self.clienteService = ClienteService()
        self.funcService = FuncionarioService()
        self.quartoService = QuartoService()
        self.reservaService = ReservaService()

        # dados iniciais
        self.cliente_padrao = Cliente("Rogério", "123", "rogerio@gmail.com", 1, "1234-5678")
        self.func_padrao = Funcionario("Peter", "123", "peter@hotel.com", 1, "Recepção")
        self.clienteService.cadastrarCliente(self.cliente_padrao)
        self.funcService.cadastrarFuncionario(self.func_padrao)

        self.quartoService.adicionarQuarto(Quarto(101, "Solteiro", 150))
        self.quartoService.adicionarQuarto(Quarto(102, "Casal", 200))

        # janela principal
        self.janela = tk.Tk()
        self.janela.title("Sistema de Hotel")

        tk.Label(self.janela, text="Login (c/f/d)").pack()
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
            messagebox.showerror("Erro", "Login inválido")
            return

        tipo = usuarios[u]["tipo"]
        self.limpar()

        if tipo == "cliente":
            self.menu_cliente()
        elif tipo == "funcionario":
            self.menu_func()
        else:
            self.menu_dono()

    # Menu do cliente
    def menu_cliente(self):
        tk.Label(self.janela, text="Menu Cliente").pack()
        tk.Button(self.janela, text="Quartos Disponíveis", command=self.ver_quartos).pack(pady=4)
        tk.Button(self.janela, text="Fazer Reserva", command=self.fazer_reserva).pack(pady=4)
        tk.Button(self.janela, text="Minhas Reservas", command=self.minhas_reservas).pack(pady=4)
        tk.Button(self.janela, text="Logout", command=self.resetar).pack(pady=4)

    def ver_quartos(self):
        msg = ""
        for q in self.quartoService.quartos:
            msg += f"Quarto {q.numero} | Tipo: {q.tipo} | Disponível: {q.disponivel}\n"
        messagebox.showinfo("Quartos", msg)

    def fazer_reserva(self):
        self.limpar()

        tk.Label(self.janela, text="Check-in (YYYY-MM-DD)").pack()
        ent1 = tk.Entry(self.janela)
        ent1.pack()

        tk.Label(self.janela, text="Check-out (YYYY-MM-DD)").pack()
        ent2 = tk.Entry(self.janela)
        ent2.pack()

        def confirmar():
            d1 = parse_data(ent1.get())
            d2 = parse_data(ent2.get())
            if not d1 or not d2:
                return

            quarto = self.quartoService.buscarDisponivel()
            if not quarto:
                messagebox.showwarning("Aviso", "Sem quartos livres!")
                return

            reserva = self.reservaService.criarReserva(1, d1, d2, self.cliente_padrao, quarto)
            if reserva:
                valor = reserva.calcularTotal()
                messagebox.showinfo("OK", f"Reserva criada! Total: R$ {valor}")
                self.menu_cliente()

        tk.Button(self.janela, text="Confirmar", command=confirmar).pack()
        tk.Button(self.janela, text="Voltar", command=self.menu_cliente).pack(pady=5)

    def minhas_reservas(self):
        msg = ""
        for r in self.reservaService.reservas:
            if r.cliente.nome == self.cliente_padrao.nome:
                msg += f"Reserva {r.idReserva} - Quarto {r.quarto.numero}\n"
        if msg == "": msg = "Nenhuma reserva encontrada."
        messagebox.showinfo("Minhas reservas", msg)

    # Menu do funcionário
    def menu_func(self):
        tk.Label(self.janela, text="Menu Funcionário").pack()
        tk.Button(self.janela, text="Listar Reservas", command=lambda: self.msg_lista(self.reservaService.listarReservas())).pack(pady=4)
        tk.Button(self.janela, text="Listar Quartos", command=lambda: self.msg_lista(self.quartoService.listarQuartos())).pack(pady=4)
        tk.Button(self.janela, text="Logout", command=self.resetar).pack(pady=4)

    def msg_lista(self, texto):
        messagebox.showinfo("Informação", texto)


    # Menu do dono
    def menu_dono(self):
        tk.Label(self.janela, text="Menu Dono").pack()
        tk.Button(self.janela, text="Listar Funcionários", command=lambda: self.msg_lista(self.funcService.listarFuncionarios)).pack(pady=4)
        tk.Button(self.janela, text="Listar Quartos", command=lambda: self.msg_lista(self.quartoService.listarQuartos)).pack(pady=4)
        tk.Button(self.janela, text="Logout", command=self.resetar).pack(pady=4)

    def resetar(self):
        self.limpar()
        self.__init__()

if __name__ == "__main__":
    InterfaceHotel()

import tkinter as tk
from tkinter import messagebox

# Função para exibir mensagens dentro do Tkinter

def mostrar_msg(msg):
    messagebox.showinfo("Informação", msg)

# Interface principal

def abrir_interface(servico=None):
    janela = tk.Tk()
    janela.title("Sistema de Hotel - Interface")
    janela.geometry("350x350")

    tk.Label(janela, text="Sistema de Hotel", font=("Arial", 16)).pack(pady=10)

    # Botão de criar reserva
    tk.Button(
        janela,
        text="Realizar Reserva",
        width=20,
        command=lambda: mostrar_msg("Reserva realizada com sucesso!")
    ).pack(pady=5)

    # Botão de listar reservas
    tk.Button(
        janela,
        text="Listar Reservas",
        width=20,
        command=lambda: mostrar_msg("Lista de reservas:")
    ).pack(pady=5)

    # Botão de sair
    tk.Button(
        janela,
        text="Sair",
        width=15,
        command=janela.destroy
    ).pack(pady=20)

    janela.mainloop()
