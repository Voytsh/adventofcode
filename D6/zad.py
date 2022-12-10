def zad(N):
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D6/input.txt', 'r') as f:
        file_contents = f.read()
        for i in range(len(file_contents) - (N - 1)):
            tmp = set(file_contents[i: i + N])
            if len(tmp) == N:
                print(i + N)
                return


if __name__ == '__main__':
    zad(4)
    zad(14)
