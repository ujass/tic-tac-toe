

class Game:
    def __init__(self):
        self.boxes = []
        self.players = []
        self.action = 1
        self.winner = None
        self.turn = 0       # 0 means, player 1 & 1 means, player 2

    def add_boxes(self, box_row):
        self.boxes.append(box_row)

    def add_players(self, player):
        self.players.append(player)

    def start_game(self):

        print('Game is started please enter the valid coordinated to play')
        while self.action < 10 and not self.winner:

            self.print_game()

            x, y = list(map(int, input('Enter x,y coordinate').split()))

            self.boxes[x][y].state = self.turn + 1

            self.turn = (self.turn + 1) % 2

            self.winner = self.check_winner()

            self.action += 1

        if self.winner:
            print('\t=============================')
            print(f'winner is player = {self.players[self.winner-1].name}')
        else:
            print(f'match is draw')

    def print_game(self):
        for i in range(3):
            for j in range(3):
                print(self.boxes[i][j], end=' ')
            print()

    def check_winner(self):
        """
        check row & col & diagonals
        if any one is filled then that person is winner.
        :return:
        """

        # check row
        for i in range(3):
            player_1 = 0
            player_2 = 0
            for j in range(3):
                if self.boxes[i][j].state == 1:
                    player_1 += 1
                elif self.boxes[i][j].state == 2:
                    player_2 += 1

            if player_1 == 3:
                return 1

            if player_2 == 3:
                return 2

        # check col
        for j in range(3):
            player_1 = 0
            player_2 = 0

            for i in range(3):

                if self.boxes[i][j].state == 1:
                    player_1 += 1
                elif self.boxes[i][j].state == 2:
                    player_2 += 1

            if player_1 == 3:
                return 1

            if player_2 == 3:
                return 2


        # left diagoanl
        player_1 = 0
        player_2 = 0
        for i in range(3):
            if self.boxes[i][i].state == 1:
                player_1 += 1
            elif self.boxes[i][i].state == 2:
                player_2 += 1

        if player_1 == 3:
            return 1

        if player_2 == 3:
            return 2

        # right diagonal
        player_1 = 0
        player_2 = 0

        i = 0
        j = 2

        while i < 3 and j >= 0:

            if self.boxes[i][j].state == 1:
                player_1 += 1
            elif self.boxes[i][j].state == 2:
                player_2 += 1

            i += 1
            j -= 1

        if player_1 == 3:
            return 1

        if player_2 == 3:
            return 2

        return None
