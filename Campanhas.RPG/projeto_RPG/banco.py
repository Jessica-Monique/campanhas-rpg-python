import sqlite3

def conectar():
    conexao = sqlite3.connect('campanhas.db')
    cursor = conexao.cursor()
    return conexao, cursor

if __name__ == "__main__":
    conexao, cursor = conectar()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campanhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            numero_jogadores INTEGER,
            sessoes INTEGER,
            data_inicio TEXT,
            data_fim TEXT 
        )
    ''')
    
    conexao.commit()
    conexao.close()

    print("Tabela 'campanhas' criada com sucesso!😁")



#Aprendi que, para poder usar valores fora de uma função, eu preciso retornar esses valores com o return dentro da função. Ao fazer isso, eu consigo acessar o que foi retornado fora dela.
#Além disso, quando eu retorno mais de um valor, como a conexão e o cursor do banco de dados, eu faço uma desestruturação de tuplas. Isso significa que eu posso separar os valores retornados e atribuí-los a variáveis individuais de forma prática, como conexao, cursor = conectar().
#Esses conceitos têm me ajudado a organizar melhor meu código e tornar minha aplicação mais modular e eficiente'''