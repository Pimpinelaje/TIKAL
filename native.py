import sqlite3

conn = sqlite3.connect('tikal_db.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Cliente (id INTEGER PRIMARY KEY NOT NULL UNIQUE, 
            nome TEXT UNIQUE, rg INTEGER UNIQUE, cpf INTEGER UNIQUE, datanasc INTEGER UNIQUE, sexo CHAR)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Telefone (id INTEGER PRIMARY KEY NOT NULL,
            ddd INTEGER, numero INTEGER NOT NULL UNIQUE, tipo TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Email (id INTEGER PRIMARY KEY NOT NULL UNIQUE,
            email TEXT)''')

print('Escolha sua ação!')
action = int(input('Digite 1 para Cadastrar cliente.\n'
                   'Digite 2 para Consultar cliente.\n'
                   'Digite 3 para Alterar dados do cliente.\n'
                   'Digite 4 para Excluir cliente.'))

if action == 1:
    nome = input('Digite o nome:')
    rg = input('Digite o RG:')
    cpf = input('Digite o CPF:')
    datanasc = input('Digite a data de nascimento:')
    sexo = str(input('Digite M para masculino e F para feminino:'))
    cur.execute('INSERT INTO Cliente (nome, rg, cpf, datanasc, sexo) VALUES (?, ?, ?, ?, ?)', (nome, rg, cpf, datanasc, sexo))

    ddd = int(input('Digite o DDD:'))
    numero = int(input('Digite o número do telefone:'))
    tipo = str(input('Digite o tipo, residencial, celular ou comercial'))
    cur.execute('INSERT INTO Telefone (ddd, numero, tipo) VALUES (?, ?, ?)', (ddd, numero, tipo))

    email = str(input('Digite o email:'))
    cur.execute('INSERT INTO Email (email) VALUES (?)', (email, ))

elif action == 2:
    email = str(input('Digite o email:'))
    cur.execute('SELECT email FROM Email WHERE email = ?', (email, ))

elif action == 3:
    nome = input('Digite o nome:')
    rg = input('Digite o RG:')
    cpf = input('Digite o CPF:')
    datanasc = input('Digite a data de nascimento:')
    sexo = str(input('Digite M para masculino e F para feminino:'))
    cur.execute('UPDATE Cliente SET (nome, rg, cpf, datanasc, sexo) WHERE = (?, ?, ?, ?, ?)',
                (nome, rg, cpf, datanasc, sexo))

    ddd = int(input('Digite o DDD:'))
    numero = int(input('Digite o número do telefone:'))
    tipo = str(input('Digite o tipo, residencial, celular ou comercial'))
    cur.execute('UPDATE Telefone SET (ddd, numero, tipo) WHERE = (?, ?, ?)', (ddd, numero, tipo))

    email = str(input('Digite o email:'))
    cur.execute('UPDATE Email SET (email) WHERE = ?', (email,))

elif action == 4:
    nome = input('Digite o nome:')
    rg = input('Digite o RG:')
    cpf = input('Digite o CPF:')
    datanasc = input('Digite a data de nascimento:')
    sexo = str(input('Digite M para masculino e F para feminino:'))
    cur.execute('DELETE FROM Cliente (nome, rg, cpf, datanasc, sexo) WHERE = (?, ?, ?, ?, ?)',
                (nome, rg, cpf, datanasc, sexo))

    ddd = int(input('Digite o DDD:'))
    numero = int(input('Digite o número do telefone:'))
    tipo = str(input('Digite o tipo, residencial, celular ou comercial'))
    cur.execute('DELETE FROM Telefone (ddd, numero, tipo) WHERE = (?, ?, ?)', (ddd, numero, tipo))

    email = str(input('Digite o email:'))
    cur.execute('DELETE FROM Email (email) WHERE = ?', (email,))

conn.commit()
cur.close()
