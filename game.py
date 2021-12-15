from snake import Snake
from board import  Board
from apple import Apple
from bomb import Bomb
import game_display




class Game:
    def __init__ (self):
        self.__snake_game = Snake((10,10),3,"Up")
        self.__board_game = Board()
        self.__apples_game = self.initial_apples()
        self.__bomb_game = self.initial_bomb()
        self.__game_values = {}
        for row in range (self.__board_game.get_height()):
            for col in range(self.__board_game.get_width()):
                for apple in self.__apples_game:
                    if apple.get_location()[0]== row and apple.get_location()[1]==col:
                        self.__game_values[(row,col)] = "green"
                if self.__bomb_game.get_position()[0][0]== row and self.__bomb_game.get_position()[0][1]==col:
                    self.__game_values[(row,col)] = "red"
                for i in range (0,len(self.__snake_game.starting_tuples())):
                    if row == self.__snake_game.get_position()[i][0] and col ==self.__snake_game.get_position()[i][1]:
                        self.__game_values[(row, col)] = "black"

    def initial_apples(self):
        apples_list = []
        apples_positions = []
        apple = Apple()
        while apple.get_location() in self.__snake_game.get_position():
            apple = Apple
        apples_positions.append(apple)
        apples_list.append(apple)
        apple = Apple()
        for i in range (0,2):
            while (apple.get_location() in self.__snake_game.get_position()) and (apple.get_location() in apples_positions):
                apple = Apple()
            apples_positions.append(apple.get_location())
            apples_list.append(apple)
            apple = Apple()
        return apples_list


    def initial_bomb(self):
        bomb =Bomb()
        apples_positions = []
        for apple in self.__apples_game:
            apples_positions.append(apple.get_location())
        while (bomb.get_position() in self.__snake_game.get_position()) or (bomb.get_position() in apples_positions):
            bomb = Bomb()
        return bomb



    def get_game_value(self):
        return self.__game_values


    def snake_eat_apple(self):
        for apple in self.__apples_game:
            if apple.get_location() == self.__snake_game.get_position():
                self.__board_game[apple.get_location()] = "black"
                new_apple = Apple()
                self.__apples_game.append(new_apple)
                ##TODO every iteration to that self.__snake_game.eat_apple()

    def snake_meets_bomb(self):
        for bomb in self.__bomb_game.get_position():
            if bomb == self.__snake_game.get_position():
                # TODO terminates game
                pass

    # TODO snake out of borders

    def apple_bomb(self):
        for bomb in self.__bomb_game.get_position():
            for apple in self.__apples_game:
                if apple.get_location() == bomb:
                    apple_loc  = apple.get_location()
                    self.__game_values.pop(apple_loc)
                    new_apple = Apple()
                    self.__apples_game.append(new_apple)

    def snake_move(self, key_clicked):
        self.__snake_game.snake_move(key_clicked)
        for row in range(self.__board_game.get_height()):
            for col in range(self.__board_game.get_width()):
                if (row, col) in self.__snake_game.get_position():
                    self.__game_values[(row, col)] = "black"

    def meetings(self):
        self.snake_meets_bomb()
        self.apple_bomb()
        self.snake_eat_apple()

