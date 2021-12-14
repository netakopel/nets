import game_parameters
import game_display

class Board:
    def __init__(self):
        self.__height = game_parameters.HEIGHT
        self.__width = game_parameters.WIDTH
        self.__board_values = []
        board_values_row = []
        for row in range (self.__height):
            for col in range (self.__width):
                board_values_row.append(((self.__height-1)-row,col))
            self.__board_values.append(board_values_row)
            board_values_row = []

    def __str__(self):
        return str(self.__board_values)





