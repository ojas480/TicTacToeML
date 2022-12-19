import numpy as np

class State:
    def __init__(self, p1, p2):
        self.board = np.zeros((3,3))
        self.p1 = p1
        self.p2 = p2
        self.boardHash = None
        # init p1 plays first
        self.playerSymbol = 1

    def getHash(self):
        self.boardHash = str(self.board.reshape(9))
        return self.boardHash

    def availablePositions(self):
        positions = []
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    positions.append((i, j))  # need to be tuple
        return positions

    def updateState(self, position):
        self.board[position] = self.playerSymbol
        # switch to another player
        self.playerSymbol = -1 if self.playerSymbol == 1 else 1

    def winner(self):
            # row
            for i in range(3):
                if sum(self.board[i, :]) == 3:
                    self.isEnd = True
                    return 1
                if sum(self.board[i, :]) == -3:
                    self.isEnd = True
                    return -1
            # col
            for i in range(3):
                if sum(self.board[:, i]) == 3:
                    self.isEnd = True
                    return 1
                if sum(self.board[:, i]) == -3:
                    self.isEnd = True
                    return -1
            # diagonal
            diag_sum1 = sum([self.board[i, i] for i in range(3)])
            diag_sum2 = sum([self.board[i, 3 - i - 1] for i in range(3)])
            diag_sum = max(abs(diag_sum1), abs(diag_sum2))
            if diag_sum == 3:
                self.isEnd = True
                if diag_sum1 == 3 or diag_sum2 == 3:
                    return 1
                else:
                    return -1

            # tie
            # no available positions
            if len(self.availablePositions()) == 0:
                self.isEnd = True
                return 0
            # not end
            self.isEnd = False
            return None

    # only when game ends
    def giveReward(self):
            result = self.winner()
            # backpropagate reward
            if result == 1:
                self.p1.feedReward(1)
                self.p2.feedReward(0)
            elif result == -1:
                self.p1.feedReward(0)
                self.p2.feedReward(1)
            else:
                self.p1.feedReward(0.1)
                self.p2.feedReward(0.5)