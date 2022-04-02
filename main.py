from src.game import Game
from src.box import Box
from src.player import Player

if __name__ == '__main__':

    game = Game()

    for i in range(3):
        boxes = []
        for j in range(3):
            boxes.append(Box(i ,j))

        game.add_boxes(boxes)

    game.add_players(Player(input('Enter player 1 name')))
    game.add_players(Player(input('Enter player 2 name')))
    game.start_game()