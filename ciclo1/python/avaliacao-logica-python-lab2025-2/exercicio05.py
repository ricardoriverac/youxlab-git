def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da sua tarefa: ").strip()
    if nome:
        tarefas.append({"nome": nome, "concluida": False})
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    else:
        print("O nome da tarefa não pode ser adicionada")
        
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa adicionada")
        return
    print("Listar tarefas:")
    for i, tarefas in enumerate(tarefas, start=1):
        marcacao = "[x]" if tarefas["concluida"] else "[ ]"
        print(f"{marcacao} {i} - {tarefas['nome']}")
    print()
    
def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        indice = int(input("Digite o número da tarefa a marcar como concluída: ")) -1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print(f"Tarefa '{tarefas[indice]['nome']} marcada como concluída!")
        else:
            print("Numero da tarefa inválido")
    except ValueError:
        print("Invalída")
            
def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    
    try:
        indice = int(input("Digite o numero da tarefa que deseja remover: ")) -1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa: '{removida['nome']}' removida!")
        else: 
            print("Não existe esta tarefa")
    except ValueError:
        print("Invalído")
            
def menu():
    tarefas = []
    while True:
        print("→ Menu de tarefas ←")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo")
            break
        else:
            print("Invalido")
            
if __name__ == "__main__":
    menu()        