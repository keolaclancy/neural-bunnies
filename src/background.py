from src.ground import Ground


# This class defines the background.
# It should only be instantiated once.
# We ned a ground, a sky
class Background:

    def __init__(self):
        self.color = 255, 255, 255

    # How do we build the ground.
    # Returns a ground object.
    def build_ground(self, height, width):

        return Ground(height, width)
