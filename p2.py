import sqlite3 as sqli
from status import Status
from obra import Obra
from engenheiro import Engenheiro
from equipe import Equipe

def conectar_banco():
    try:
        con = sqli.connect("appdb.db")
        return con
    except sqli.Error as e:
        print("Erro ao conectar -", e)

conexao = conectar_banco()

def criar_tabela_status():
    sql = """
            create table if not exists status (
                codigo integer not null primary key autoincrement,
                descricao text not null
            )
          """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Tabela STATUS criada com sucesso!")
    except sqli.Error as e:
        print("Erro ao criar a tabela STATUS!", e)
        conexao.rollback()

def criar_tabela_obra():
    sql = """
            create table if not exists obra (
                codigo integer not null primary key autoincrement,
                nome text not null,
                local text not null,
                status int not null,
                FOREIGN KEY (status) REFERENCES status(codigo)
            )
          """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Tabela OBRA criada com sucesso!")
    except sqli.Error as e:
        print("Erro ao criar a tabela OBRA!")
        conexao.rollback()

def criar_tabela_engenheiro():
    sql = """
            create table if not exists engenheiro (
                codigo integer not null primary key autoincrement,
                nome text not null,
                identificacao text not null
            )
          """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Tabela ENGENHEIRO criada com sucesso!")
    except sqli.Error as e:
        print("Erro ao criar a tabela ENGENHEIRO!")
        conexao.rollback()

def criar_tabela_equipe():
    sql = """
            create table if not exists equipe (
                obra integer not null,
                engenheiro int not null,
                horas int not null,
                FOREIGN KEY (engenheiro) REFERENCES engenheiro(codigo)
                FOREIGN KEY (obra) REFERENCES obra(codigo)
            )
          """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Tabela EQUIPE criada com sucesso!")
    except sqli.Error as e:
        print("Erro ao criar a tabela EQUIPE!")
        conexao.rollback()

def inserir_status():

    descricao = input("Digite a descricao do status:")
    status = Status(descricao)

    sql = f"""
            insert into status(descricao) values 
            ('{status.descricao}')
          """
    
    try:
        cursor = conexao.cursor()
        cursor.execute(sql).lastrowid
        conexao.commit()
        print("STATUS add com sucesso!")
    except sqli.Error as e:
        conexao.rollback()
        print("Erro ao cadastrar STATUS")

def inserir_engenheiro():

    nome = input("Digite o nome do engenheiro:")
    identificacao = input("Digite a identificacao do engenheiro:")
    engenheiro = Engenheiro(nome, identificacao)

    sql = f"""
            insert into engenheiro(nome, identificacao) values 
            ('{engenheiro.nome}', '{engenheiro.identificacao}')
          """
    
    try:
        cursor = conexao.cursor()
        cursor.execute(sql).lastrowid
        conexao.commit()
        print("ENGENHEIRO add com sucesso!")
    except sqli.Error as e:
        conexao.rollback()
        print("Erro ao cadastrar ENGENHEIRO", e)

def inserir_obra():

    nome = input("Digite o nome da obra:")
    local = input("Digite o local da obra:")
    status = input("Digite o status da obra:")
    obra = Obra(nome, local, status)

    sql = f"""
            insert into obra(nome, local, status) values 
            ('{obra.nome}', '{obra.local}', {obra.status})
          """
    
    try:
        cursor = conexao.cursor()
        cursor.execute(sql).lastrowid
        conexao.commit()
        print("OBRA add com sucesso!")
    except sqli.Error as e:
        conexao.rollback()
        print("Erro ao cadastrar OBRA", e)

def inserir_obra():

    nome = input("Digite o nome da obra:")
    local = input("Digite o local da obra:")
    status = input("Digite o status da obra:")
    obra = Obra(nome, local, status)

    sql = f"""
            insert into obra(nome, local, status) values 
            ('{obra.nome}', '{obra.local}', {obra.status})
          """
    
    try:
        cursor = conexao.cursor()
        cursor.execute(sql).lastrowid
        conexao.commit()
        print("OBRA add com sucesso!")
    except sqli.Error as e:
        conexao.rollback()
        print("Erro ao cadastrar OBRA", e)

def inserir_equipe():

    obra = input("Digite a obra:")
    engenheiro = input("Digite o engenheiro:")
    horas = input("Digite a hora:")
    equipe = Equipe(obra, engenheiro, horas)

    sql = f"""
            insert into equipe(obra, engenheiro, horas) values 
            ('{equipe.obra}', '{equipe.engenheiro}', {equipe.horas})
          """
    
    try:
        cursor = conexao.cursor()
        cursor.execute(sql).lastrowid
        conexao.commit()
        print("EQUIPE add com sucesso!")
    except sqli.Error as e:
        conexao.rollback()
        print("Erro ao cadastrar EQUIPE", e)

def listar_obras():

    id = int(input("Forneça o ID do engenheiro:"))

    sql = f"""
        SELECT equipe.engenheiro, obra.nome, status.descricao
        from equipe
        inner join obra on obra.codigo = equipe.obra
        inner join status on status.codigo = obra.status
        WHERE equipe.engenheiro = {id}
    """

    cursor = conexao.cursor()
    resultado = cursor.execute(sql).fetchall()

    if resultado:
        print("Engenheiro\tObra\t\tStatus")
        print("-" * 50)
        for row in resultado:
            print(f"{row[0]}\t\t{row[1]}\t{row[2]}")

def main() :
    
    print("------------------------MENU----------------------------")
    opcao = int(input("Digite 1 para listar as obras de um engenheiro:"))

    if(opcao == 1):
        listar_obras()
    else:
        print("Programa encerrado!")

main()