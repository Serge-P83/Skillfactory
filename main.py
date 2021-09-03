board = list(range(1, 10))

combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def drawboard():
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')


def ask(player_move):
    while True:
        vol = input('ход игрока:' + player_move)
        if not (vol in '123456789'):
            print('Неверный ход')
            continue
        vol = int(vol)
        if str(board[vol - 1]) in 'XO':
            print('Занято!')
            continue
        board[vol - 1] = player_move
        break


def wins():
    for every in combination:
        if (board[every[0] - 1]) == (board[every[1] - 1]) == (board[every[2] - 1]):
            return board[every[1] - 1]
    else:
        return False


def main():
    count = 0
    while True:
        drawboard()
        if count % 2 == 0:
            ask('X')
        else:
            ask('O')
        if count > 3:
            winner = wins()
            if winner:
                drawboard()
                print(winner, 'Победа!')
                break
        count += 1
        if count > 8:
            drawboard()
            print('Ничья')
            break


main()
