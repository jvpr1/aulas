from datetime import date, time
from typing import List
from sqlalchemy import ForeignKey, String, Integer, Date, Time, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Veiculo(Base):
    __tablename__ = "veiculos"

    id: Mapped[int] = mapped_column(primary_key=True)
    chasi_numero: Mapped[str] = mapped_column(String(17), unique=True)
    capacidade: Mapped[int] = mapped_column(Integer)
    inspecao_tecnica: Mapped[date] = mapped_column(Date)
    tipo: Mapped[str] = mapped_column(String(20))

    # Relacionamento 1:N (Um Veículo tem várias Rotas)
    rotas: Mapped[List["Rota"]] = relationship(back_populates="veiculo")

    def verificar_inspecao(self):
        pass


class Motorista(Base):
    __tablename__ = "motoristas"

    id: Mapped[int] = mapped_column(primary_key=True)
    cpf: Mapped[str] = mapped_column(String(11), unique=True)
    nome: Mapped[str] = mapped_column(String(100))
    cnh: Mapped[str] = mapped_column(String(20), unique=True)
    telefone: Mapped[int] = mapped_column(Integer)

    # Relacionamento 1:N (Um Motorista tem várias Rotas)
    rotas: Mapped[List["Rota"]] = relationship(back_populates="motorista")

    def iniciar_rota(self):
        pass

    def encerrar_rota(self):
        pass


class Rota(Base):
    __tablename__ = "rotas"

    id: Mapped[int] = mapped_column(primary_key=True)
    codigo: Mapped[int] = mapped_column(Integer, unique=True)
    descricao: Mapped[str] = mapped_column(String(255))
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    horario: Mapped[time] = mapped_column(Time)

    # Chaves Estrangeiras
    veiculo_id: Mapped[int] = mapped_column(ForeignKey("veiculos.id"))
    motorista_id: Mapped[int] = mapped_column(ForeignKey("motoristas.id"))

    # Relacionamentos inversos
    veiculo: Mapped["Veiculo"] = relationship(back_populates="rotas")
    motorista: Mapped["Motorista"] = relationship(back_populates="rotas")
    
    # Relacionamento 1:N
    alunos: Mapped[List["Aluno"]] = relationship(back_populates="rota")

    def adicionarAluno(self):
        pass

    def removerAluno(self):
        pass

    def validarAluno(self):
        pass

    def iniciar(self):
        pass

    def encerrar(self):
        pass


class Aluno(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    matricula: Mapped[int] = mapped_column(Integer, unique=True)
    endereco: Mapped[str] = mapped_column(String(255))
    escola: Mapped[str] = mapped_column(String(100))
    turno: Mapped[time] = mapped_column(Time)

    # Chave Estrangeira da Rota (Relacionamento 1:N)
    rota_id: Mapped[int] = mapped_column(ForeignKey("rotas.id"))
    rota: Mapped["Rota"] = relationship(back_populates="alunos")

    # Relacionamento 1:1 (Um Aluno tem uma Presença)
    presenca: Mapped["Presenca"] = relationship(back_populates="aluno", uselist=False)

    def cadastrar(self):
        pass

    def validar_RFID(self):
        pass

    def consultar_presenca(self):
        pass


class Presenca(Base):
    __tablename__ = "presencas"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[date] = mapped_column(Date)
    horarioEntrada: Mapped[time] = mapped_column(Time)
    status: Mapped[bool] = mapped_column(Boolean)

    # Chave Estrangeira do Aluno (Relacionamento 1:1)
    aluno_id: Mapped[int] = mapped_column(ForeignKey("alunos.id"), unique=True)
    aluno: Mapped["Aluno"] = relationship(back_populates="presenca")

    def registrar(self):
        pass

    def consultar(self):
        pass
