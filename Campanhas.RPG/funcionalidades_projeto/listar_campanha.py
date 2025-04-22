from projeto_RPG.banco import conectar

def listar_campanha():
    conexao, cursor = conectar()

    cursor.execute('SELECT * FROM campanhas')
    campanhas = cursor.fetchall()

    if len(campanhas) == 0:
        print("Nenhuma campanha cadastrada")
    else:
        for campanha in campanhas:
            print(f"ID: {campanha[0]}")
            print(f"Nome: {campanha[1]}")
            print(f"Descrição: {campanha[2]}")
            print(f"Numero de Jogadores: {campanha[3]}")
            print(f"Sessões: {campanha[4]}")
            print(f"Início: {campanha[5]}")
            print(f"Fim: {campanha[6]}")
            print("-" * 30)
    
    conexao.close()

if __name__ == "__main__":
    listar_campanha()