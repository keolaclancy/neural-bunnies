import random


# Obstacle
# Has a position
# Has a size
# Has a color
# Has a speed (fixed)
class Obstacle:

    def __init__(self, ground_height, width):

        self.foot_level = ground_height
        self.screen_width = width
        self.size_x = 24
        self.size_y = 16
        self.pos_x = width + random.randint(50, 200)  # @todo: This should be handle by obstacle manager.
        self.pos_y = self.foot_level - self.size_y
        self.color = 245, 35, 20
        self.speed = 5
