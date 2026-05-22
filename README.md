``# Sistema de Transporte Escolar

## 1. Lista de Requisitos

### Requisitos Funcionais (RF)

RF01 – Cadastro de veículos  
O sistema deve permitir cadastrar ônibus e vans contendo placa, capacidade e data da última inspeção técnica.

RF02 – Cadastro de alunos  
O sistema deve permitir cadastrar alunos com endereço, escola e turno.

RF03 – Cadastro de rotas  
O sistema deve permitir cadastrar rotas contendo motorista, veículo e pontos de parada.

RF04 – Associação de alunos às rotas  
O sistema deve permitir vincular alunos a uma rota específica.

RF05 – Registro de presença via RFID  
O sistema deve registrar o horário de entrada do aluno ao passar a carteirinha no sensor.

RF06 – Validação de aluno na rota  
O sistema deve validar se o aluno pertence à rota antes de registrar sua presença.

RF07 – Verificação da inspeção técnica  
O sistema deve verificar se o veículo possui inspeção válida antes de iniciar a rota.

RF08 – Bloqueio de início da rota  
O sistema deve bloquear o início da viagem caso a inspeção esteja vencida.

RF09 – Notificação para a central  
O sistema deve notificar a central quando houver tentativa de iniciar rota com inspeção vencida.

---

### Requisitos Não Funcionais (RNF)

RNF01 – Segurança  
O sistema deve permitir acesso apenas a usuários autorizados.

RNF02 – Desempenho  
A validação do RFID deve ocorrer rapidamente.

RNF03 – Disponibilidade  
O sistema deve funcionar durante os horários escolares.

RNF04 – Armazenamento  
O sistema deve manter histórico de presença dos alunos.

---

# 2. Casos de Uso

```mermaid
flowchart LR

Administrador((Administrador))
Motorista((Motorista))
Central((Central))
RFID((Sensor RFID))

CadastroVeiculo[Cadastro de Veiculos]
CadastroAluno[Cadastro de Alunos]
CadastroRota[Cadastro de Rotas]
AssociarAluno[Associar Alunos as Rotas]
Historico[Consultar Historico de Presenca]

IniciarRota[Iniciar Rota]
ConsultarRota[Consultar Rota]
Bloqueio[Bloquear Inicio da Rota]

RegistrarRFID[Registrar Presenca via RFID]
ValidarAluno[Validar Aluno na Rota]

Notificacao[Receber Notificacao]
Monitoramento[Monitorar Rotas]

Administrador --> CadastroVeiculo
Administrador --> CadastroAluno
Administrador --> CadastroRota
Administrador --> AssociarAluno
Administrador --> Historico

Motorista --> IniciarRota
Motorista --> ConsultarRota

RFID --> RegistrarRFID
RFID --> ValidarAluno

Central --> Notificacao
Central --> Monitoramento

IniciarRota --> Bloqueio
RegistrarRFID --> ValidarAluno
```

---

# 3. Diagrama de Estrutura

```mermaid
classDiagram

class Veiculo {
    +placa : String
    +capacidade : int
    +dataUltimaInspecao : Date
}

class Aluno {
    +nome : String
    +endereco : String
    +escola : String
    +turno : String
}

class Motorista {
    +nome : String
    +cnh : String
}

class Rota {
    +codigo : int
    +pontosParada : String
}

class Presenca {
    +horarioEntrada : DateTime
}

class SensorRFID {
    +registrarPresenca()
}

class Central {
    +notificar()
}

Rota --> Veiculo
Rota --> Motorista
Rota --> Aluno
Aluno --> Presenca
SensorRFID --> Presenca
Rota --> Central
```

---

# 4. Diagrama de Classes

```mermaid
classDiagram

class Veiculo{
    +String placa
    +int capacidade
    +date inspecao_tecnica
    +String tipo

    verificar_inspecao()
    iniciar_rota()
    bloquear_rota()
}

class Aluno{
    +String nome
    +int matricula
    +String endereco
    +String escola
    +time turno

    cadastrar()
    validar_RFID()
    consultar_presenca()
}

class Rota{
    +int codigo
    +String descricao
    +bool status
    +time horario

    adicionarAluno()
    removerAluno()
    validarAluno()
    iniciar()
    encerrar()
}

class Presenca{
    +date data
    +time horarioEntrada
    +bool status

    registrar()
    consultar()
}

class Motorista{
    +String cpf
    +String nome
    +String cnh
    +int telefone

    iniciar_rota()
    encerrar_rota()
}

Rota "1" -- "*" Aluno
Aluno "1" -- "*" Presenca
Veiculo "1" -- "*" Rota
Motorista "1" -- "*" Rota
```

---

# 5. Diagrama de Sequência

```mermaid
sequenceDiagram
Motorista->>Sistema: iniciar rota
Sistema->>Veiculo: verificar inspecao

alt inspecao valida
    Veiculo-->>Sistema: ok
    Sistema-->>Motorista: rota iniciada
else inspecao vencida
    Veiculo-->>Sistema: vencida
    Sistema-->>Motorista: rota bloqueada
    Sistema->>Central: notificar central
end

Aluno->>RFID: passar cartao
RFID->>Sistema: enviar RFID
Sistema->>Rota: validar aluno

alt aluno valido
    Rota-->>Sistema: permitido
    Sistema-->>Aluno: presenca confirmada
else aluno invalido
    Rota-->>Sistema: negado
    Sistema-->>Aluno: acesso negado
end
```
