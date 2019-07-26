import pygame
from src.background import Background
from src.interface import Interface
from src.obstacle_manager import ObstacleManager


# This class manages the display of everything.
class Display:

    def __init__(self):
        # Debug.
        self.debug = False

        # Colors.
        self.white = 255, 255, 255
        self.green = 100, 175, 130
        self.red = 245, 35, 20
        self.blue = 0, 0, 255

        #images
        self.image_night_sky = pygame.image.load('ressources/images/background/night_sky.png')
        self.image_obstacle = pygame.image.load('ressources/images/obstacles/spike_a.png')

        # Init screen.
        self.size = self.width, self.height = 640, 480
        self.screen = pygame.display.set_mode(self.size)

        self.test_surface = pygame.Surface((320, 240))

        # Define the bg class
        self.bg = Background()

        # Define the obstacle manager class
        self.ground = Background.build_ground(self.bg, self.height, self.width)
        self.om = ObstacleManager(self.ground.height, self.width)

        # Define the interface class
        self.interface = Interface(self.screen, self.height, self.width)

    # Display the background.
    def show_background(self):
        # Fill the bg color
        self.screen.fill(self.bg.color)

        # Display the sky
        image = pygame.transform.scale(self.image_night_sky, (self.width, self.ground.height))
        self.screen.blit(image, (0, 0))

        # Build the ground.
        pygame.draw.line(
            self.screen,
            self.ground.color,
            (self.ground.start, self.ground.height), (self.ground.end, self.ground.height)
        )

    # Display the score.
    def show_score(self, player):
        score = player.score_counter()

        # Use the interface to position the text.
        self.interface.display_score(score)

    # Display the obstacles.
    def show_obstacles(self):

        # Get the obstacles and draw them.
        obstacles = self.om.run()

        # self.debug = True
        for obstacle in obstacles:
            if self.debug:
                obstacle_pos = obstacle.pos_x, obstacle.pos_y
                obstacle_size = obstacle.size_x, obstacle.size_y
                pygame.draw.rect(self.screen, obstacle.color, (obstacle_pos, obstacle_size))

            image = pygame.transform.scale(self.image_obstacle, (24, 24))
            self.screen.blit(image, (obstacle.pos_x, obstacle.pos_y - 3))

    def check_collision(self, player):
        self.om.check_collision(player)

    # Display the score.
    def show_end_screen(self, player):
        score = player.score_counter()

        self.interface.display_end_screen(score)

    # Reset the game. player pos and obstacle pos.
    def reset(self, player):
        player.score = 0
        player.dead = False
        self.om.clear_all_obstacles()
