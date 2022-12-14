def get_section_assignment():
    lista = []
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D4/d4.txt', 'r') as f:
        for line in f:
            pair = line.split(",")
            tmp = [pair[0], pair[1].strip()]
            lista.append(tmp)
    return lista


def get_answer(lista):
    idxs_part1, idxs_part2 = [], []
    for index, item in enumerate(lista, start=1):
        first_elf_int = list(map(int, item[0].split("-")))
        second_elf_int = list(map(int, item[1].split("-")))

        if (second_elf_int[0] <= first_elf_int[0] <= second_elf_int[1]) or (
                second_elf_int[0] <= first_elf_int[1] <= second_elf_int[1]) or (
                first_elf_int[0] <= second_elf_int[0] <= first_elf_int[1]) or (
                first_elf_int[0] <= second_elf_int[1] <= first_elf_int[1]):
            idxs_part2.append(index)

        if (first_elf_int[0] <= second_elf_int[0]) and (first_elf_int[1] >= second_elf_int[1]) or (
                (first_elf_int[0] >= second_elf_int[0]) and (first_elf_int[1] <= second_elf_int[1])):
            idxs_part1.append(index)
    return idxs_part1, idxs_part2


if __name__ == '__main__':
    part1_answer, part2_answer = get_answer(get_section_assignment())
    print(f"Answer: {len(part1_answer), len(part2_answer)}")
