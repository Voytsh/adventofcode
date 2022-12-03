def shape_selected_points(x):
    return {
        'A': 1,
        'B': 2,
        'C': 3,
    }[x]

def round_outcome_points(tuple):
    win = 6
    tie = 3
    lose = 0

    if tuple[0] == tuple[1]:
        #print("It's a tie!")
        return tie
    elif tuple == ('A', 'B') or tuple == ('B', 'C') or tuple == ('C', 'A'):
        return win
    elif tuple == ('B', 'A') or tuple == ('C', 'B') or tuple == ('A', 'C'):
        return lose
    else:
        print("ERROR")
        exit(-1)

def translate(x):
    return {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }[x]

#def single_round_score(shape, outcome):


def jazda():
    cc = 0
    total_score = 0
    single_round_score = 0
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D2/d2.txt', 'r') as f:
        for line in f:
            my_tuple = (line[0], translate(line[2]))
            cc += 1
            round_points = round_outcome_points(my_tuple) + shape_selected_points(translate(line[2]))
            print(f"#{cc} {my_tuple}, You scored {round_points} points")
            total_score += round_points
        print(f" Your total score is {total_score}")



if __name__ == '__main__':
    jazda()


