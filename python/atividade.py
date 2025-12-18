from sqlalchemy import create_engine, text

DB_URL = "mysql+pymysql://root:@localhost:5506/taaskflow_db?charset=utf8mb4"
engine = create_engine(DB_URL, echo=False, future=True)



def inserirU():
    nome = input("Digite seu nome: ")

    with engine.connect() as conn:
        query = text("INSERT INTO usuarios (nome) VALUES (:nome)")
        conn.execute(query, {"nome": nome})
        conn.commit()

    print(f"Olá, {nome}! Usuário cadastrado com sucesso.")


def listar_U():
    try:
        with engine.connect() as conn:
            query = text("SELECT id_usuario, nome FROM usuarios")
            result = conn.execute(query)

            print("\n--- Usuários Cadastrados ---")
            for row in result:
                print(f"{row.id_usuario} - {row.nome}")
    except Exception as e:
        print(e)


def inserirT():
    descricao = input("Descrição da tarefa: ")
    usuario_id = input("ID do usuário responsável: ")

    with engine.connect() as conn:
        query = text("""
            INSERT INTO tarefas (descricao, usuario_id)
            VALUES (:descricao, :usuario_id)
        """)
        conn.execute(query, {"descricao": descricao, "usuario_id": usuario_id})
        conn.commit()

    print("Tarefa cadastrada com sucesso!")


    def listar_T():
        print("1 - Listar todas")
        print("2 - Listar por usuário")
    opc = input("Escolha: ")

    with engine.connect() as conn:
        if opc == "1":
            query = text("SELECT * FROM tarefas")
            result = conn.execute(query)
        else:
            uid = input("ID do usuário: ")
            query = text("SELECT * FROM tarefas WHERE usuario_id = :uid")
            result = conn.execute(query, {"uid": uid})

    print("\n--- Tarefas ---")
    for row in result:
        print(f"{row.id} - {row.descricao} (User {row.usuario_id})")


def atualizar_T():
    tarefa_id = input("ID da tarefa: ")
    nova_desc = input("Nova descrição: ")

    with engine.connect() as conn:
        query = text("""
            UPDATE tarefas 
            SET descricao = :desc 
            WHERE id = :tid
        """)
        conn.execute(query, {"desc": nova_desc, "tid": tarefa_id})
        conn.commit()

    print("Tarefa atualizada!")

    def remover_T():
         
         tarefa_id = input("ID da tarefa: ")
         with engine.connect() as conn:
           query = text("DELETE FROM tarefas WHERE id = :tid")
           conn.execute(query, {"tid": tarefa_id})
           conn.commit()

    print("Tarefa removida!")


    def remover_T():
         tarefa_id = input("ID da tarefa: ")
         with engine.connect() as conn:
          query = text("DELETE FROM tarefas WHERE id = :tid")
          conn.execute(query, {"tid": tarefa_id})
         conn.commit()

    print("Tarefa removida!")



inserirU








       
    

