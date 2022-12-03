def get_rucksacks():
    lista = []
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D3/d3.txt', 'r') as f:
        for line in f:
            lista.append(line.strip())
    return lista


def get_priority_value(x):
    if (90 >= ord(x) >= 65):  # UPPERCASE
        return (ord(x) - 38)

    if (122 >= ord(x) >= 96):  # lowercase
        return (ord(x) - 96)

    print("tak jak pan jezus powiedzial")


def find_common_items(lista):
    common_lista = []
    common_item_for_one_group = set()
    for i in range(0, 300, 3):
        common_item_for_one_group = set(lista[i]).intersection(set(lista[i + 1]))
        common_item_for_one_group = common_item_for_one_group.intersection(set(lista[i + 2]))
        common_lista.append(common_item_for_one_group)
    return common_lista


if __name__ == '__main__':
    raksaki = get_rucksacks()
    common_items = find_common_items(raksaki)

    result = 0
    for item in common_items:
        result += get_priority_value((list(item)[0]))
    print(f"Total priority value = {result}")
