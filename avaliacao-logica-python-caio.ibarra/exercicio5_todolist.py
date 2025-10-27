tarefas = []

def adicionartarefa():
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("Tarefa adicionada!\n")
    listartarefas()


def listartarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    
    for i, tarefa in enumerate(tarefas):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i+1} - {tarefa['titulo']}")
    print()  


def marcarconcluida():
    listartarefas()
    if not tarefas:
        return
    numero = int(input("Digite o número da tarefa para marcar como concluída: "))

    if 1 <= numero <= len(tarefas):
        tarefas[numero-1]["concluida"] = True
        print("Tarefa marcada como concluída!\n")
    else:
        print("Número inválido!\n")


def removertarefa():
    listartarefas()
    if not tarefas:
        return
    
    numero = int(input("Digite o número da tarefa para remover: "))
    if 1 <= numero <= len(tarefas):
        removed = tarefas.pop(numero-1)
        print(f"Tarefa '{removed['titulo']}' removida!\n")
    else:
        print("Número inválido!\n")


while True:
    print("------ GERENCIADOR DE TAREFAS ------")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionartarefa()

    elif opcao == "2":
        listartarefas()

    elif opcao == "3":
        marcarconcluida()

    elif opcao == "4":
        removertarefa()

    elif opcao == "5":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.\n")

