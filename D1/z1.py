if __name__ == '__main__':
    tmp = 0
    one_elf_total_calories = []
    with open('d1z1.txt') as f:
        for line in f:
            if line != '\n':
                tmp += int(line)
            else:
                one_elf_total_calories.append(tmp)
                tmp = 0

        bq = max(one_elf_total_calories)
        print(f'The most calories in total of {bq} is carried by the elf #{one_elf_total_calories.index(bq)}')



