from collections import Counter
from io import StringIO

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def play_bingo(game_numbers, game_boards):
    board_marks = dict()
    for drawn_number in game_numbers:
        for board_number, board in enumerate(game_boards):
            row, col = check_board(board, drawn_number)
            if row is None:
                continue
            # Add to board results and check for winner!
            board_score = board_marks.get(board_number, [[], []])
            board_score[0].append(row)
            board_score[1].append(col)
            board_marks[board_number] = board_score
            if winner_board(board_score):
                return board_number, board_score, drawn_number
    return None, None, None


def check_board(board, number):
    for row_number in range(len(board)):
        for col_number in range(len(board[row_number])):
            if board[row_number][col_number] == number:
                return row_number, col_number
    return None, None


def winner_board(check_score):
    row_count = Counter(check_score[0])
    col_count = Counter(check_score[1])
    if row_count.most_common(1)[0][1] == 5:
        return True
    elif col_count.most_common(1)[0][1] == 5:
        return True
    else:
        return False


bingo_numbers = []
boards = []
input_src = open('bingo_data.txt')
#input_src = StringIO(test_data)

with input_src as data:
    # Read numbers
    number_line = data.readline()
    bingo_numbers = number_line.strip().split(',')
    loading_board = []
    for data_line in data:
        if len(data_line) == 1:
            loading_board = []
            boards.append(loading_board)
            continue
        col_list = []
        for num_slice in [(0, 2), (3, 5), (6, 8), (9, 11), (12, 14)]:
            col_list.append(data_line[num_slice[0]:num_slice[1]].strip())
        loading_board.append(col_list)

while len(boards) > 0:
    board_number, marked, last_number = play_bingo(bingo_numbers, boards)
    card = boards[board_number]
    boards.remove(card)

if marked is not None:
    print(f'winner! {marked} {card}')
    marked_row_col = list(zip(marked[0],marked[1]))
    card_score = 0
    for r_id, row in enumerate(card):
        for c_id, col in enumerate(row):
            if (r_id,c_id) not in marked_row_col:
                card_score += int(col)
    print(card_score * int(last_number))






