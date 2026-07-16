# Crie um programa que funcione como uma lista de tarefas (To-Do List) com as seguintes funcionalidades:

# Menu principal com as opções:
# 1 → Adicionar nova tarefa
# 2 → Listar todas as tarefas
# 3 → Marcar tarefa como concluída
# 4 → Remover uma tarefa
# 5 → Sair

tarefas = []
while True:
    print('Escolha uma opção')
    menu = input('[a]dicionar [l]istar [c]oncluir [r]emover [s]air: ').lower()
    if menu == 'a':
        adicionar = input('Adicione uma tarefa: ')
        tarefas.append(adicionar)
        print(f'Voce adicionou "{adicionar}" a sua lista de tarefas.')
        print(f'Lista atualizada: {tarefas}')
    if menu == 'l':
        print('Tarefas atuais')
        for i, t in enumerate(tarefas, start=1):
            print(f'{i}. {t}')
    if menu == 'c':
        if not tarefas:
            print('Nao ha tarefas para concluir.')
        else:
            for i, t in enumerate(tarefas, start=1):
                print(f'{i}. {t}')
            try:
                concluir = int(input('Digite o numero da tarefa: '))
                concluida = tarefas.pop(concluir - 1)
                print(f'Voce concluiu a tarefa "{concluida}".')
                print(f'Tarefas restantes: {tarefas}')
            except (ValueError, IndexError):
                print('Numero invalido. Tente novamente.')
    if menu == 'r':
        print('Escolha uma tarefa para remover:')
        for i, t in enumerate(tarefas, start=1):
            print(f'{i}. {t}')
        remover = int(input('Digite o numero da tarefa: '))
        removida = tarefas.pop(remover - 1)
        print(f'Voce removeu a tarefa "{removida}"')
        print(f'Lista atualizada: {tarefas}')
    if menu == 's':
        print('Voce saiu do program de tarefas!!')
        break