from copy import deepcopy


class ticTacToe:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def print_board(self):
        print("""Board:
{} | {} | {}
----------
{} | {} | {}
----------
{} | {} | {}""".format(self.board[0][0], self.board[0][1], self.board[0][2], self.board[1][0], self.board[1][1],
                       self.board[1][2], self.board[2][0], self.board[2][1], self.board[2][2]))

    def get_board(self):
        return self.board

    def avaliable_moves(self, input_board):
        moves = []
        for row in input_board:
            for value in row:
                if value != "X" and value != "O":
                    moves.append(int(value))
        return moves

    def has_won(self, input_board, player):
        won = False
        if [player, player, player] in input_board:
            won = True
        if input_board[0][0] == player and input_board[1][0] == player and input_board[2][0] == player:
            won = True
        if input_board[0][1] == player and input_board[1][1] == player and input_board[2][1] == player:
            won = True
        if input_board[0][2] == player and input_board[1][2] == player and input_board[2][2] == player:
            won = True
        if input_board[0][0] == player and input_board[1][1] == player and input_board[2][2] == player:
            won = True
        if input_board[0][2] == player and input_board[1][1] == player and input_board[2][0] == player:
            won = True
        return won

    def make_move(self, input_board, position, player):
        for i in range(len(input_board)):
            for j in range(3):
                if (str(position) == input_board[i][j]):
                    input_board[i][j] = player

    def game_over(self, input_board):
        if len(self.avaliable_moves(input_board)) == 0:
            return True
        if self.has_won(input_board, "X") == True:
            return True
        if self.has_won(input_board, "O") == True:
            return True
        return False

    def evaluate_board(self, input_board):
        if self.has_won(input_board, "X"):
            return 1
        if self.has_won(input_board, "O"):
            return -1
        return 0

    def minimax(self, input_board, is_maximizing):
        if self.game_over(input_board):
            return [self.evaluate_board(input_board), ""]
        best_move = ""
        if is_maximizing:
            best_value = -float("Inf")
            symbol = "X"
        else:
            best_value = float("Inf")
            symbol = "O"
        for move in self.avaliable_moves(input_board):
            new_board = deepcopy(input_board)
            self.make_move(new_board, move, symbol)
            hypothetical_value = self.minimax(new_board, not is_maximizing)[0]
            if is_maximizing == True and hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
            if is_maximizing == False and hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
        return [best_value, best_move]

    def make_best_move(self, input_board, player):
        max = False
        if player == "X":
            max = True
        best_move = self.minimax(input_board, max)
        self.make_move(self.board, best_move[1], player)


if __name__ == '__main__':
    game = ticTacToe()
    board = game.get_board()

    while not game.game_over(board):
        board = game.get_board()
        game.print_board()
        person_move = int(input("You are X, Choose where you want to place your move.\n"))
        while not (person_move in game.avaliable_moves(board)):
            person_move = int(input("That is not a possible move. Please try again.\n"))
        game.make_move(board, person_move, "X")

        if game.game_over(board):
            break
        board = game.get_board()
        game.print_board()
        print("AI choosing move...")
        game.make_best_move(board, "O")

        if game.game_over(board):
            break

    board = game.get_board()
    game.print_board()
    if game.has_won(board, "X"):
        print("You Win!")
    elif game.has_won(board, "O"):
        print("You Lost")
    else:
        print("Tie!")


