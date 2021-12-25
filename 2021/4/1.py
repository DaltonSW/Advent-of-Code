import copy

SQUARE_SIZE = 5

class Board():
    def __init__(self):
        self.rows = []

    rows = []

    def checkBingo(self):
        for i in range(SQUARE_SIZE):
            if (self.rows[i][0] == 'xx' and self.rows[i][1] == 'xx' and self.rows[i][2] == 'xx' and self.rows[i][3] == 'xx' and self.rows[i][4] == 'xx'):
                return True

            if (self.rows[0][i] == 'xx' and self.rows[1][i] == 'xx' and self.rows[2][i] == 'xx' and self.rows[3][i] == 'xx' and self.rows[4][i] == 'xx'):
                return True

        if (self.rows[0][0] == 'xx' and self.rows[1][1] == 'xx' and self.rows[2][2] == 'xx' and self.rows[3][3] == 'xx' and self.rows[4][4] == 'xx'):
                return True    
        
        if (self.rows[4][0] == 'xx' and self.rows[3][1] == 'xx' and self.rows[2][2] == 'xx' and self.rows[1][3] == 'xx' and self.rows[0][4] == 'xx'):
                return True


def main():
    f = open('4/input.txt', 'r')
    numbers = f.readline().split(',')

    f.readline() # clear extra blank line

    rawBoards = f.readlines()

    f.close() # don't forget it

    boards = []
    tempBoard = Board()

    for line in rawBoards:
        if line == '\n':
            boards.append(copy.deepcopy(tempBoard))
            tempBoard = Board()
            tempBoard.rows.clear()
        
        else:
            tempBoard.rows.append(line.strip().split())

    printBoards(boards)
    for number in numbers:
        print("Calling: {}".format(number))
        for index, board in enumerate(boards):
            if markBoard(board, number):
                print("Mark on board {}".format(index))
            if board.checkBingo():
                winningBoard(board, number)
                return
        


def printBoards(boards):
    for i in range(len(boards)-1):
        print("\nBoard {}".format(i))
        for row in boards[i].rows:
            print("{} {} {} {} {}".format(row[0], row[1], row[2], row[3], row[4]))

def markBoard(board, number):
    for row in board.rows:
        for index, num in enumerate(row):
            if num == number:
                row[index] = 'xx'
                return True
    return False

def winningBoard(board, lastCall):
    unmarked = 0
    for row in board.rows:
        for num in row:
            if num != 'xx':
                unmarked += int(num)

    print("BINGO! -- Answer: {}".format(int(unmarked) * int(lastCall)))

main()




# get text into boards
# develop an algorithm to check board for bingo
# figure out how to mark a spot on the board (x's maybe?)