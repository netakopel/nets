from typing import Optional, Any, List
from game_parameters import get_random_apple_data

class Apple():
    def __init__(self):
        self.__location = (get_random_apple_data()[0], get_random_apple_data()[1])
        self.__score = get_random_apple_data()[2]


