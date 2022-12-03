def get_common_items():
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D3/d3.txt', 'r') as f:
        common_list = []
        for line in f:
            firstpart, secondpart = line[:len(line) // 2], line[len(line) // 2:]
            common_list.append(set(firstpart).intersection(set(secondpart)))
        return common_list


def get_priority_value(x):
    if (90 >= ord(x) >= 65):  # UPPERCASE
        return (ord(x) - 38)

    if (122 >= ord(x) >= 96):  # lowercase
        return (ord(x) - 96)

    print("tak jak pan jezus powiedzial")


if __name__ == '__main__':
    lista = get_common_items()
    get_priority_value("a")

    result = 0
    for item in lista:
        result += get_priority_value((list(item)[0]))
    print(f"Total priority value = {result}")
