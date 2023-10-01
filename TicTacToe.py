def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = -1, -1

        while (
            row not in range(1, 4)
            or col not in range(1, 4)
            or board[row - 1][col - 1] != " "
        ):
            try:
                row, col = map(
                    int,
                    input(
                        f"Player {player}, enter row (1-3) and column (1-3) separated by space: "
                    ).split(),
                )
            except ValueError:
                pass

        board[row - 1][col - 1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
