import random

class random_number_generator:
    
    @staticmethod
    def getRandomGameNumber(total_game_number):
        return random.randint(0, total_game_number)
    
    @staticmethod
    def getOneOrTwo():
        return random.randint(1, 2)