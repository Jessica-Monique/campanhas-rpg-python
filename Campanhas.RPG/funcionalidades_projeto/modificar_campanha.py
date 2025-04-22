from projeto_RPG.banco import conectar

def modificar_campanha():
    conexao, cursor = conectar()

    cursor.execute('SELECT id, nome FROM campanhas')
    campanhas = cursor.fetchall()

    if not campanhas:
        print("Nehuma Campanha cadastrada.")
        conexao.close()
        return

    print("\n Campanhas cadastradas: ")
    for campanha in campanhas:
        print(f"ID:{campanha[0]} | Nome:{campanha[1]}")

    #seleciona a camapnha pelo ID
    id_campanha = input("\n Digite o ID da campanha que deseja modificar: ")
    cursor.execute('SELECT * FROM campanhas WHERE id = ?', (id_campanha,))
    campanha_selecionada = cursor.fetchone()

    if not campanha_selecionada:
        print("Nenhuma campanha encontrada com esse ID. ")
        conexao.close()
        return 
        
    # Mostra opcoes de campos para modificar
    print("\n O que deseja Modificar ? ")
    print("1 - Nome ")
    print("2 - Descrição ")
    print("3 - Número de Jodgadores ")
    print("4 - Sessões ")
    print("5 - Data de Início ")
    print("6 - Data de Fim ")

    opcao = input("Digite o número da opção desejada: ")

    campos = {
        "1": "nome",
        "2": "descricao",
        "3": "numero_jogadores",
        "4": "sessoes",
        "5": "data_inicio",
        "6": "data_fim"
    }

    if opcao not in campos:
        print("Opção Inválida. ")
        conexao.close()
        return

    novo_valor = input(f"Digite um novo valor para {campos[opcao]}: ")

    #atualizar no banco de dados
    cursor.execute(f'UPDATE campanhas SET {campos[opcao]} = ? WHERE id = ?', (novo_valor, id_campanha))
    conexao.commit()
    print("Campanha atualizada com sucesso!")

    conexao.close()

if __name__ =="__main__":
    modificar_campanha()