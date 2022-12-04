def get_section_assignment():
    lista = []
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D4/d4.txt', 'r') as f:
        for line in f:
            pair = line.split(",")
            tmp = [pair[0], pair[1].strip()]
            lista.append(tmp)
    return lista


def get_pairs_that_fully_contain_other(lista):
    idxs = []
    for index, item in enumerate(lista, start=1):
        first_elf = item[0]
        second_elf = item[1]
        first_elf = first_elf.split("-")
        second_elf = second_elf.split("-")
        first_elf_int = list(map(int, first_elf))
        second_elf_int = list(map(int, second_elf))

        if (first_elf_int[0] <= second_elf_int[0]) and (first_elf_int[1] >= second_elf_int[1]) or (
                (first_elf_int[0] >= second_elf_int[0]) and (first_elf_int[1] <= second_elf_int[1])):
            idxs.append(index)
            print(index, first_elf, second_elf)

    return idxs


def get_pairs_that_overlap(lista):
    idxs = []
    for index, item in enumerate(lista, start=1):
        first_elf = item[0]
        second_elf = item[1]
        first_elf_int = list(map(int, first_elf.split("-")))
        second_elf_int = list(map(int, second_elf.split("-")))

        if (second_elf_int[0] <= first_elf_int[0] <= second_elf_int[1]) or (
                second_elf_int[0] <= first_elf_int[1] <= second_elf_int[1]) or (
                first_elf_int[0] <= second_elf_int[0] <= first_elf_int[1]) or (
                first_elf_int[0] <= second_elf_int[1] <= first_elf_int[1]):
            idxs.append(index)
            print(index, first_elf, second_elf)

    return idxs


if __name__ == '__main__':
    lista = get_section_assignment()
    # x = get_pairs_that_fully_contain_other(lista)
    x = get_pairs_that_overlap(lista)
    print(f"Answer: {len(x)}")
