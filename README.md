# 🏨 Sistema de Reservas de Hotel - POO

## 📋 Descrição

Sistema completo de gerenciamento de reservas de hotel desenvolvido em Python, aplicando os princípios de **Programação Orientada a Objetos (POO)**. Oferece interface gráfica moderna e intuitiva (Tkinter) com três níveis de acesso: Dono, Funcionário e Cliente.

## 🎯 Objetivos do Projeto

Demonstrar a aplicação prática dos conceitos fundamentais de POO:
- ✅ **Herança e Polimorfismo**
- ✅ **Composição e Agregação**
- ✅ **Encapsulamento com Properties**
- ✅ **Abstração**
- ✅ **Validações de Regras de Negócio**
- ✅ **Documentação Completa (Docstrings)**
- ✅ **Arquitetura em Camadas (MVC)**
- ✅ **Princípios SOLID**
- ✅ **Interface Gráfica Moderna**

---

## 📁 Estrutura do Projeto

```
Trabalho-III-Trimestre---POO/
│
├── models/                      # 📦 Camada de Modelos (Domain)
│   ├── __init__.py             # Inicializador do pacote
│   ├── pessoa.py               # Classe abstrata Pessoa
│   ├── cliente.py              # Classe Cliente (herda de Pessoa)
│   ├── funcionario.py          # Classe Funcionario (herda de Pessoa)
│   ├── quarto.py               # Classe Quarto
│   └── reserva.py              # Classe Reserva (composição)
│
├── interface/                   # 🎨 Camada de Apresentação
│   ├── __init__.py             # Exporta HotelApp
│   ├── app.py                  # Aplicação principal
│   ├── login.py                # Tela de login
│   ├── base_interface.py       # Classe base com menu lateral
│   ├── interface_dono.py       # Interface do dono
│   ├── interface_funcionario.py# Interface do funcionário
│   ├── interface_cliente.py    # Interface do cliente
│   ├── componentes.py          # Componentes reutilizáveis
│   ├── cores.py                # Paleta de cores
│   └── estilos.py              # Estilos TTK
│
├── services.py                  # 🔧 Camada de Serviços (Business Logic)
├── main.py                      # 🚀 Ponto de entrada
├── teste.py                     # 🧪 Testes unitários
├── README.md                    # 📖 Documentação (este arquivo)
│
└── diagramas/                   # 📊 Diagramas UML
    ├── caso_uso.png             # Diagrama de casos de uso
    └── classes.png              # Diagrama de classes
```

---

## 🏗️ Arquitetura

### Arquitetura em Camadas (Layered Architecture)

```
┌─────────────────────────────────────┐
│   INTERFACE (Presentation Layer)   │  ← Tkinter GUI
├─────────────────────────────────────┤
│   SERVICES (Business Logic Layer)  │  ← Regras de Negócio
├─────────────────────────────────────┤
│   MODELS (Domain Layer)            │  ← Entidades do Sistema
└─────────────────────────────────────┘
```

### 📦 Camada de Modelos (Models)

Representa as entidades do domínio com suas regras intrínsecas.

#### 1. **Pessoa** (Classe Abstrata - ABC)
- **Papel**: Classe base para Cliente e Funcionario
- **Atributos**: `nome`, `documento` (CPF), `email`
- **Método Abstrato**: `exibirDados()`
- **Validações**:
  - Nome: não pode ser vazio
  - CPF: exatamente 11 dígitos numéricos
  - Email: formato válido com @ e domínio

#### 2. **Cliente** (Herda de Pessoa)
- **Herança**: Estende `Pessoa`
- **Atributos Adicionais**: `idCliente`, `telefone`, `senha`
- **Validações**:
  - Telefone: mínimo 8 dígitos
  - Senha: mínimo 3 caracteres
  - ID auto-gerado se não fornecido

#### 3. **Funcionario** (Herda de Pessoa)
- **Herança**: Estende `Pessoa`
- **Atributos Adicionais**: `idFuncionario`, `cargo`, `senha`
- **Métodos**: `revisarQuarto()`
- **Validações**:
  - Cargo: não pode ser vazio
  - Senha: mínimo 3 caracteres
  - ID auto-gerado se não fornecido

#### 4. **Quarto**
- **Atributos**: `numero`, `tipo`, `precoDiaria`, `disponivel`
- **Métodos**: `marcarOcupado()`, `liberarQuarto()`
- **Validações**:
  - Número: inteiro positivo
  - Preço: valor positivo
  - Tipo: string não vazia

#### 5. **Reserva**
- **Composição**: Possui `Cliente` e `Quarto`
- **Atributos**: `idReserva`, `dataCheckin`, `dataCheckout`, `valorTotal`
- **Métodos**: `calcularTotal()`, `confirmarReserva()`, `cancelarReserva()`
- **Validações**:
  - Checkout > Checkin
  - Quarto deve estar disponível
  - Valor calculado automaticamente
  - ID auto-gerado se não fornecido

### 🔧 Camada de Serviços (Services)

Implementa a lógica de negócio e coordena operações entre modelos.

#### **ClienteService**
- `criar()` - Cria e cadastra novo cliente
- `editar()` - Edita dados de cliente existente
- `excluir()` - Remove cliente do sistema
- `listarClientes()` - Lista todos os clientes
- `buscarPorEmail()` - Busca cliente por email
- `buscarPorId()` - Busca cliente por ID

**Permissões**: Dono e Funcionário podem gerenciar clientes

#### **FuncionarioService**
- `criar()` - Cria e cadastra novo funcionário
- `editar()` - Edita dados de funcionário
- `excluir()` - Remove funcionário
- `listarFuncionarios()` - Lista todos os funcionários
- `buscarPorEmail()` - Busca funcionário por email
- `buscarPorId()` - Busca funcionário por ID

**Permissões**: Apenas Dono pode gerenciar funcionários

#### **QuartoService**
- `criar()` - Cria e cadastra novo quarto
- `listarQuartos()` - Lista todos os quartos
- `listarDisponiveis()` - Lista apenas quartos disponíveis
- `buscarDisponivel()` - Busca primeiro quarto disponível

#### **ReservaService**
- `criarReserva()` - Cria nova reserva
- `cancelar()` - Cancela reserva e libera quarto
- `listarReservas()` - Lista todas as reservas
- `buscarPorCliente()` - Busca reservas de um cliente
- `buscarPorId()` - Busca reserva por ID

### 🎨 Camada de Interface (GUI)

Interface gráfica moderna desenvolvida com Tkinter/ttk.

#### **Estrutura de Componentes**

- **HotelApp**: Gerencia janela principal e navegação
- **TelaLogin**: Autenticação de usuários
- **BaseInterface**: Classe base com menu lateral
- **InterfaceDono**: Interface completa para administrador
- **InterfaceFuncionario**: Interface limitada para funcionário
- **InterfaceCliente**: Interface de visualização e reservas
- **FormularioBase**: Componente de formulário reutilizável
- **TabelaModerna**: Componente de tabela estilizada

#### **Esquema de Cores**

- **Primária**: `#2C3E50` (Azul escuro profissional)
- **Destaque**: `#3498DB` (Azul claro)
- **Sucesso**: `#27AE60` (Verde)
- **Erro**: `#E74C3C` (Vermelho)
- **Aviso**: `#F39C12` (Laranja)
- **Texto Claro**: `#FFFFFF`
- **Texto Escuro**: `#2C3E50`

---

## 🎓 Conceitos de POO Implementados

### 1. ✅ Herança
```python
# Pessoa é classe abstrata base
class Pessoa(ABC):
    ...

# Cliente herda de Pessoa
class Cliente(Pessoa):
    ...

# Funcionario herda de Pessoa
class Funcionario(Pessoa):
    ...
```

### 2. ✅ Polimorfismo
```python
# Método abstrato implementado de forma diferente em cada classe
class Pessoa(ABC):
    @abstractmethod
    def exibirDados(self):
        pass

class Cliente(Pessoa):
    def exibirDados(self):
        print(f"Cliente: {self.nome} - CPF: {self.documento}")

class Funcionario(Pessoa):
    def exibirDados(self):
        print(f"Funcionário: {self.nome} - Cargo: {self.cargo}")
```

### 3. ✅ Encapsulamento
```python
class Cliente(Pessoa):
    def __init__(self, nome, ...):
        self._telefone = None  # Atributo privado
    
    @property
    def telefone(self):
        """Getter - Retorna telefone"""
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        """Setter - Valida antes de atribuir"""
        digitos = re.sub(r'\D', '', valor)
        if len(digitos) < 8:
            raise ValueError("Telefone deve ter no mínimo 8 dígitos")
        self._telefone = valor
```

### 4. ✅ Composição
```python
# Reserva possui (tem-um) Cliente e Quarto
class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, ...):
        self._cliente = cliente
        self._quarto = quarto
```

### 5. ✅ Abstração
```python
from abc import ABC, abstractmethod

class Pessoa(ABC):
    """Classe abstrata - não pode ser instanciada"""
    
    @abstractmethod
    def exibirDados(self):
        """Método abstrato - deve ser implementado pelas subclasses"""
        pass
```

---

## 🔐 Funcionalidades por Tipo de Usuário

### 👑 Dono (Administrador)

**Dashboard:**
- 📊 Estatísticas gerais do sistema
- 👥 Total de clientes
- 👨‍💼 Total de funcionários
- 🛏️ Total de quartos
- ✅ Quartos disponíveis
- 📅 Total de reservas

**Funcionalidades:**
- ✅ Cadastrar, editar e excluir clientes
- ✅ Cadastrar, editar e excluir funcionários
- ✅ Cadastrar quartos
- ✅ Criar reservas
- ✅ Visualizar todas as listas e reservas
- ✅ Acesso total ao sistema

### 👨‍💼 Funcionário

**Dashboard:**
- 📊 Estatísticas resumidas
- 👥 Total de clientes
- ✅ Quartos disponíveis
- 📅 Reservas ativas

**Funcionalidades:**
- ✅ Cadastrar, editar e excluir clientes
- ✅ Listar clientes, quartos e funcionários
- ✅ Visualizar reservas
- ❌ Não pode gerenciar funcionários
- ❌ Não pode cadastrar quartos

### 👤 Cliente

**Funcionalidades:**
- ✅ Visualizar quartos disponíveis
- ✅ Fazer novas reservas
- ✅ Ver suas próprias reservas
- ✅ Cancelar suas reservas
- ✅ Cálculo automático do valor total

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.7+** (recomendado 3.10 ou superior)
- **Tkinter** (geralmente incluído com Python)

### Instalação

1. **Clone ou baixe o repositório**

2. **Navegue até a pasta do projeto:**
```bash
cd "Trabalho-III-Trimestre---POO"
```

### Executar o Sistema

**Interface Gráfica (Recomendado):**
```bash
python main.py
```

**Executar Testes:**
```bash
python teste.py
```

---

## 👥 Credenciais de Acesso

### Login Padrão

| Tipo | Email/Usuário | Senha |
|------|---------------|-------|
| 👑 **Dono** | `dono@hotel.com` ou `dono` | `123` |
| 👨‍💼 **Funcionário** | `bruno@hotel.com` | `123` |
| 👤 **Cliente** | `jordan@email.com` | `123` |

---

## 🧪 Testes Unitários

O arquivo `teste.py` contém testes abrangentes para validar:

### Testes Implementados:

1. **✅ Teste de Cliente**
   - Criação de cliente
   - Validações de CPF, email, telefone
   - Properties funcionando corretamente

2. **✅ Teste de Funcionário**
   - Criação de funcionário
   - Validações de cargo e credenciais
   - Método `revisarQuarto()`

3. **✅ Teste de Quarto**
   - Criação de quarto
   - Validações de número e preço
   - Marcação ocupado/disponível

4. **✅ Teste de Reserva**
   - Criação de reserva
   - Validações de datas
   - Cálculo automático de valor
   - Cancelamento de reserva

5. **✅ Teste de Services**
   - CRUD de clientes e funcionários
   - Controle de permissões
   - Verificação de duplicatas
   - Busca por email e ID

6. **✅ Teste de Herança e Polimorfismo**
   - Verificação de herança
   - Polimorfismo de `exibirDados()`

7. **✅ Teste de Encapsulamento**
   - Properties validando dados
   - Exceções sendo lançadas corretamente

**Executar todos os testes:**
```bash
python teste.py
```

**Saída esperada:**
```
==================== TESTES DO SISTEMA ====================
[OK] Cliente criado e validado
[OK] Funcionario criado e validado
[OK] Quarto criado e gerenciado
[OK] Reserva criada e cancelada
[OK] Services funcionando
[OK] Heranca implementada
[OK] Encapsulamento funcionando
===========================================================
✅ TODOS OS TESTES PASSARAM!
```

---

## 📊 Diagramas UML

Os diagramas estão localizados na pasta `diagramas/`:

### 📈 Diagrama de Casos de Uso
**Arquivo**: `diagramas/caso_uso.jpg`

Mostra as interações entre os atores (Dono, Funcionário, Cliente) e o sistema.

### 📐 Diagrama de Classes
**Arquivo**: `diagramas/classes.jpeg`

Apresenta a estrutura completa das classes, seus atributos, métodos e relacionamentos.

**Relacionamentos Principais:**

```
       Pessoa (ABC)
          ↑
    ┌─────┴─────┐
    │           │
Cliente    Funcionario

Reserva
  ├── possui → Cliente
  └── possui → Quarto
```

---

## 🔒 Validações Implementadas

### Validações de Dados

| Campo | Regra | Onde |
|-------|-------|------|
| **Nome** | Não vazio | `Pessoa.nome` (property) |
| **CPF** | Exatamente 11 dígitos numéricos | `Pessoa.documento` (property) |
| **Email** | Formato válido com @ e domínio | `Pessoa.email` (property) |
| **Telefone** | Mínimo 8 dígitos | `Cliente.telefone` (property) |
| **Senha** | Mínimo 3 caracteres | `Cliente/Funcionario.senha` (property) |
| **Cargo** | Não vazio | `Funcionario.cargo` (property) |
| **Número Quarto** | Inteiro positivo | `Quarto.numero` (property) |
| **Preço** | Positivo | `Quarto.precoDiaria` (property) |
| **Datas** | Checkout > Checkin | `Reserva` (construtor) |

### Validações de Negócio

- ✅ CPF não pode ser duplicado (Services)
- ✅ Quarto deve estar disponível para reserva
- ✅ Apenas dono pode cadastrar funcionários
- ✅ Dono e funcionário podem cadastrar clientes
- ✅ Cliente só vê suas próprias reservas