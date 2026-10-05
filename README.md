# 🏥 Sistema Hospitalar - Gestão de Pacientes (CRUD)

Este é um sistema simples de gestão de pacientes desenvolvido em **Python** integrado com uma base de dados **Oracle SQL**. O projeto foi construído para demonstrar operações fundamentais de **CRUD** (Create, Read, Update, Delete) com persistência de dados.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.x](https://www.python.org/)[cite: 1]
- **Base de Dados:** [Oracle Database](https://www.oracle.com/database/)[cite: 1]
- **Biblioteca de Conexão:** `oracledb`[cite: 1]

---

## 📌 Funcionalidades

O sistema oferece uma interface interativa via linha de comandos (CLI) com as seguintes opções:

1. **Inserir Paciente (`Create`):** Regista um novo paciente guardando Nome, Observação e Idade. O RG é gerado automaticamente pela base de dados.
2. **Listar Pacientes (`Read`):** Exibe todos os pacientes registados na base de dados ordenados pelo RG.
3. **Atualizar Idade (`Update`):** Permite alterar a idade de um paciente existente através do seu RG.
4. **Excluir Paciente (`Delete`):** Remove o registo de um paciente da base de dados através do seu RG.

---

## 🗄️ Estrutura da Tabela

A tabela `Paciente` é gerada com a seguinte estrutura SQL:

```sql
CREATE TABLE Paciente (
    rg NUMBER GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR2(25),
    observacao VARCHAR2(100),
    idade NUMBER(100,2),
    PRIMARY KEY (rg)
);
