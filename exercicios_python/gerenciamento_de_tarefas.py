# Crie um programa que funcione como uma lista de tarefas (To-Do List) com as seguintes funcionalidades:

# Menu principal com as opções:
# 1 → Adicionar nova tarefa
# 2 → Listar todas as tarefas
# 3 → Marcar tarefa como concluída
# 4 → Remover uma tarefa
# 5 → Sair

tarefas = []  # cada tarefa é um dicionário {"texto": ..., "status": ...}

while True:
    print('Escolha uma opção')
    menu = input('[a]dicionar [l]istar [c]concluir [r]emover [s]air: ').lower()

    if menu == 'a':
        adicionar = input('Adicione uma tarefa: ')
        tarefas.append({"texto": adicionar, "status": "Pendente"})  # >>>> **** ALTERAÇÃO **** adiciona com status
        print(f'Você adicionou "{adicionar}" à sua lista de tarefas.')

    if menu == 'l':
        print('Tarefas atuais')
        for i, t in enumerate(tarefas, start=1):
            print(f'{i}. {t["texto"]} - {t["status"]}')  # >>>> **** ALTERAÇÃO **** mostra status

    if menu == 'c':
        if not tarefas:
            print('Não há tarefas para concluir.')
        else:
            for i, t in enumerate(tarefas, start=1):
                print(f'{i}. {t["texto"]} - {t["status"]}')
            try:
                concluir = int(input('Digite o número da tarefa: '))
                tarefas[concluir - 1]["status"] = "Concluída"  # >>>> **** ALTERAÇÃO **** só muda status
                print(f'Tarefa "{tarefas[concluir - 1]["texto"]}" marcada como concluída.')
            except (ValueError, IndexError):
                print('Número inválido. Tente novamente.')

    if menu == 'r':
        print('Escolha uma tarefa para remover:')
        for i, t in enumerate(tarefas, start=1):
            print(f'{i}. {t["texto"]} - {t["status"]}')
        try:
            remover = int(input('Digite o número da tarefa: '))
            removida = tarefas.pop(remover - 1)  # >>>> **** ALTERAÇÃO **** remove só o índice escolhido
            print(f'Você removeu a tarefa "{removida["texto"]}".')
        except (ValueError, IndexError):
            print('Número inválido. Tente novamente.')

    if menu == 's':
        print('Você saiu do programa de tarefas!!')
        break
