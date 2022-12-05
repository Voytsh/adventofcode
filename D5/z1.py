def get_procedure():
    lista = []
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D5/procedure.txt', 'r') as f:
        for line in f:
            tmp = []
            line = line.split(" ")
            tmp.append(int(line[1]))
            tmp.append(int(line[3]))
            tmp.append(int(line[5]))
            lista.append(tmp)
    return lista


def get_init_stacks():
    lista = []
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D5/stacks.txt', 'r') as f:
        for line in f:
            for i in range(len(line)):
                if i % 4 == 1 and 64 < ord(line[i]) < 91:
                    stack_number = int((i + 3) / 4)
                    x = (stack_number, line[i])
                    lista.append(x)

        result = []
        for i in range(1, 10):
            nowa_lista = []
            for item in lista:
                if item[0] == i:
                    nowa_lista.append(item[1])
            nowa_lista.reverse()
            result.append(nowa_lista)
        return result


def move_stacks(procedure_list, init_stacks):
    for procedure in procedure_list:
        items_to_move_number = procedure[0]
        from_stack_number = procedure[1] - 1
        to_stack_number = procedure[2] - 1

        items_to_move = (init_stacks[from_stack_number][(-1 * items_to_move_number):])
        init_stacks[from_stack_number] = init_stacks[from_stack_number][: (-1 * items_to_move_number)]
        items_to_move.reverse()
        for item in items_to_move:
            init_stacks[to_stack_number].append(item)

    return init_stacks


if __name__ == '__main__':
    final_stacks = move_stacks(get_procedure(), get_init_stacks())
    for stack in final_stacks:
        print(stack[-1:])
