from projeto_RPG.banco import conectar


def inserir_campanha():
    conexao, cursor = conectar()

    nome = input("Digite o nome da campanha: ")
    descricao = input(" Descreva a campanha: ")
    numero_jogadores = input("Há quantos jogadores: ")
    sessoes = input("quantidade de sessões: ")
    data_inicio = input("Data de início (dd-mm-aaaa): ")
    data_fim = input("Data de fim (dd-mm-aaaa): ")

    cursor.execute('''
        INSERT INTO campanhas (nome, descricao, numero_jogadores, sessoes, data_inicio, data_fim )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, descricao, numero_jogadores, sessoes, data_inicio, data_fim))

    conexao.commit()
    conexao.close()

    print("Parabens! Campanha inserida 🎲 \n")    


if __name__ == "__main__":
    inserir_campanha()