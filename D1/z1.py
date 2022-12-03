def get_list_of_calories():
    tmp = 0
    result = []
    with open('D1/d1z1.txt') as f:
        for line in f:
            if line != '\n':
                tmp += int(line)
            else:
                result.append(tmp)
                tmp = 0
    return result

if __name__ == '__main__':
    one_elf_total_calories = get_list_of_calories()
    bq = max(one_elf_total_calories)

    print("z1")
    print(f'The most calories in total of {bq} is carried by the elf #{one_elf_total_calories.index(bq)}')

    print("\nz2")
    print(sum(sorted(one_elf_total_calories, reverse=True)[:3]))


