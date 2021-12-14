from game_parameters import get_random_bomb_data

class Bomb:
    def __init__ (self)-> None:
        bomb_data = get_random_bomb_data()
        self.__start_position_x = bomb_data[0]
        self.__start_position_y = bomb_data[1]
        self.__list_of_position = [(bomb_data[0],bomb_data[1])]
        self.__radius = bomb_data[2]
        self.__time = bomb_data[3]
        self.__current_radius = 0



    def update_bomb_positions(self,board_cor):
        new_list_position = []
        for row in range (len(board_cor)):
            for col in range (len(board_cor[0])):
                if abs(self.__start_position_x - row)  + abs(self.__start_position_y - col) == self.__current_radius:
                    new_list_position.append((row,col))
        self.__list_of_position = new_list_position
        self.__current_radius  += 1








