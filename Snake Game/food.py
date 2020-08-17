import random 


class Food():
    def __init__(self,width,height, snake_block):
        self.__width = width
    
        self.__snake = snake_block
            
    def get_food(self,width,height,snake_block):
        foodx = round(random.randrange(0,width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0,height - snake_block) / 10.0) * 10.0

        return foodx, foody
