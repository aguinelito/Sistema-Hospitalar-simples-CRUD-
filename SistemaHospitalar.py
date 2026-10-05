import oracledb

# --- Conexão ---
def getConnection():
    try:
        conn = oracledb.connect(
            user='rm564857',
            password='080499',
            host='oracle.fiap.com.br',
            port=1521,
            service_name="orcl"
        )
        print('Conexão com Oracle DB estabelecida')
        return conn
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
        return None

def create_table(conn):
    cursor = conn.cursor()
    try:
        sql = """
        CREATE TABLE Paciente(
            rg NUMBER GENERATED ALWAYS AS IDENTITY,
            nome VARCHAR2(25),
            observacao VARCHAR2(100),
            idade NUMBER(100,2),
            PRIMARY KEY (rg)
        )
        """
        cursor.execute(sql)
        print('Paciente registrado com sucesso')
    except oracledb.Error as e:
        print(f'Erro ao criar a tabela: {e}')

def create_paciente(nome, observacao , idade):
    print('Adicionando novo paciente' )
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO PACIENTE (nome, observacao, idade)
            VALUES (:nome, :observacao, :idade)
        """
        cursor.execute(sql, {
            'nome': nome,
            'observacao': observacao,
            'idade': idade
        })
        conn.commit()
        print(f'Paciente {nome} adicionado!')
    except oracledb.Error as e:
        print(f'Erro ao adicionar paciente: {e}')
        conn.rollback()
    finally:
        conn.close()

def read_paciente():
    print(' Lista de pacientes ')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "SELECT rg, nome, observacao, idade FROM PACIENTE ORDER BY rg"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f'RG: {row[0]}, Nome: {row[1]}, Observação: {row[2]}, Idade: {row[3]}')
    except oracledb.Error as e:
        print(f'Erro de leitura: {e}')
    finally:
        conn.close()

def update_paciente(rg, new_idade):
    print(' Atualizando paciente ')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "UPDATE PACIENTE SET idade = :new_idade WHERE rg = :rg"
        cursor.execute(sql, {'new_idade': new_idade, 'rg': rg})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Idade do paciente RG {rg} atualizada!')
        else:
            print(f'Paciente com RG {rg} não encontrado.')
    except oracledb.Error as e:
        print(f'Erro ao atualizar: {e}')
        conn.rollback()
    finally:
        conn.close()

def delete_paciente(rg):
    print(f'*** Excluindo paciente RG {rg} ***')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM PACIENTE WHERE rg = :rg"
        cursor.execute(sql, {'rg': rg})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Paciente com RG {rg} excluído!')
        else:
            print(f'Paciente com RG {rg} não encontrado.')
    except oracledb.Error as e:
        print(f'Erro ao excluir: {e}')
        conn.rollback()
    finally:
        conn.close()

# --- Menu principal ---
def main():
    while True:
        print("\n--- Menu CRUD - Tabela Paciente ---")
        print("1. Inserir novo paciente")
        print("2. Listar todos os pacientes")
        print("3. Atualizar idade de um paciente")
        print("4. Excluir um paciente")
        print("5. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            nome = input("Nome do paciente: ")
            observacao = input("Observação: ")
            try:
                idade = float(input("Idade: "))
            except ValueError:
                print("Idade inválida!")
                continue
            create_paciente(nome, observacao, idade)

        elif opcao == 2:
            read_paciente()

        elif opcao == 3:
            read_paciente()
            try:
                rg = int(input("RG do paciente para atualizar: "))
                new_idade = float(input("Nova idade: "))
            except ValueError:
                print("RG ou idade inválida!")
                continue
            update_paciente(rg, new_idade)

        elif opcao == 4:
            read_paciente()
            try:
                rg = int(input("RG do paciente para excluir: "))
            except ValueError:
                print("RG inválido!")
                continue
            delete_paciente(rg)

        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

# programa principal
main()
conn = getConnection()  # obter a conexão
print(f'Conexão: {conn.version}')