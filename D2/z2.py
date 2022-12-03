def shape_selected_points(x):
    return {
        'A': 1,
        'B': 2,
        'C': 3,
    }[x]


def round_outcome(x):
    return {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }[x]


def what_I_choose(opponents_choice, round_outcome):
    if (round_outcome == 0 and opponents_choice == "B") or (round_outcome == 3 and opponents_choice == "A") or (
            round_outcome == 6 and opponents_choice == "C"):
        return "A"
    elif (round_outcome == 0 and opponents_choice == "C") or (round_outcome == 3 and opponents_choice == "B") or (
            round_outcome == 6 and opponents_choice == "A"):
        return "B"
    elif (round_outcome == 0 and opponents_choice == "A") or (round_outcome == 3 and opponents_choice == "C") or (
            round_outcome == 6 and opponents_choice == "B"):
        return "C"


if __name__ == '__main__':
    # X means I need to lose
    # Y means I need to draw
    # Z means I need to win

    total_score = 0
    with open('/Users/filipwojcieszak/Documents/Adventofcode/D2/d2.txt', 'r') as f:
        for line in f:
            total_score += round_outcome(line[2]) + shape_selected_points(
                what_I_choose(line[0], round_outcome(line[2])))
        print(f" Your total score is {total_score}")
