from typing import Optional, Any, List

POSSIBLE_DIRECTION = ["UP", "DOWN", "LEFT", "RIGHT"]
POSSIBLE_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Snake:
    def __init__(self, start_position: tuple, length: int, direction: str):
        self.__start_position = start_position
        self.__length = length
        self.__direction = direction
        self.__list_of_positions = self.starting_tuples()

    def starting_tuples(self) -> list:
        head = self.__start_position
        lst = []
        for i in range(self.__length):
            lst.append((head[0] - i, head[1]))
        return lst

    def cut_tail(self) -> None:
        tail = self.__list_of_positions[-1]
        self.__list_of_positions.remove(tail)

    def move_up(self) -> None:
        new_head = (self.__list_of_positions[0][0] + 1, self.__list_of_positions[0][1])
        self.__list_of_positions.insert(0, new_head)
        self.__direction = "UP"
        self.cut_tail()

    def move_down(self) -> None:
        new_head = (self.__list_of_positions[0][0] - 1, self.__list_of_positions[0][1])
        self.__list_of_positions.insert(0, new_head)
        self.__direction = "DOWN"
        self.cut_tail()

    def move_left(self) -> None:
        new_head = (self.__list_of_positions[0][0], self.__list_of_positions[0][1] + 1)
        self.__list_of_positions.insert(0, new_head)
        self.__direction = "LEFT"
        self.cut_tail()

    def move_right(self) -> None:
        new_head = (self.__list_of_positions[0][0], self.__list_of_positions[0][1] - 1)
        self.__list_of_positions.insert(0, new_head)
        self.__direction = "RIGHT"
        self.cut_tail()

    def snake_move(self, key_clicked) -> None:
        if key_clicked in POSSIBLE_MOVES:
            if key_clicked == "UP" and self.__direction != "DOWN":
                self.move_up()
            if key_clicked == "DOWN" and self.__direction != "UP":
                self.move_down()
            if key_clicked == "LEFT" and self.__direction != "RIGHT":
                self.move_left()
            if key_clicked == "RIGHT" and self.__direction != "LEFT":
                self.move_right()

    def get_position(self):
        return self.__list_of_positions

    def get_direction(self):
        return self.__direction

# benet = Snake((10,10), 3, "UP")
# print(benet.starting_tuples())
# benet.move_up()
# print(benet.get_position())
# benet.move_left()
# print(benet.get_position())
# print(benet.get_direction())









