from projeto_RPG.banco import conectar

def excluir_campanha():
    conexao, cursor = conectar()

    cursor.execute('SELECT id, nome FROM campanhas')
    todas_campanhas = cursor.fetchall()

    if todas_campanhas:
        print("\n Campanhas Cadastradas:")
        for campanha in todas_campanhas:
            print(f"ID: {campanha[0]} | Nome: {campanha[1]}")
    else:
        print("Não ha nada pra excluir")
        conexao.close()
        return        

    id_exclusao = input("\n Digite o ID da Campanha que deseja excluir ")
    cursor.execute('SELECT * FROM campanhas WHERE id = ?', (id_exclusao,))
    campanha_selecionada = cursor.fetchone()

    if campanha_selecionada:
        confirmacao = input(f"Tem CERTEZA que deseja excluir a campanha {id_exclusao}? (s/n): ").lower()
        if confirmacao == 's':
            cursor.execute('DELETE FROM campanhas WHERE id = ?', (id_exclusao,))
            conexao.commit()
            print("Campanha excluida com sucesso!")
        else:
            print("Exclusão Cancelada.")
    else:
        print("Nenhuma campanha encontrada com esse ID.\n")
    
    conexao.close()

if __name__ == "__main__":
    excluir_campanha()