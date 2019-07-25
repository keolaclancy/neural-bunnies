import pygame
import random


# This is the player.
# It has a position on the screen
# It has a size
# it can jump.
# it has a score
# it has a fitness score
# It can also die
class Player(pygame.sprite.Sprite):

    image_player_up = pygame.image.load('ressources/images/player/rabbit_up.png')
    image_player_down = pygame.image.load('ressources/images/player/rabbit_down.png')
    image_player_normal = pygame.image.load('ressources/images/player/rabbit_normal.png')
    image_player_dead = pygame.image.load('ressources/images/player/rabbit_dead.png')

    def __init__(self, ground_height):
        super().__init__()

        self.foot_level = ground_height
        self.size_x = 36
        self.size_y = 32
        self.pos_x = 20
        self.pos_y = self.foot_level - self.size_y
        self.jumping = False
        self.falling = False
        self.dead = False
        self.color = 100, 175, 130
        self.status = 4  # At init the player is idle.
        self.score = 0

        self.image = self.get_player_image()
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        # Jump listener
        self.player_jump()
        # Score listener
        self.score_counter()

    # Return the image of the player.
    def get_player_image(self):
        if (self.score % 10) > 5:
            image = self.image_player_normal
        else:
            image = self.image_player_down

        if self.jumping:
            image = self.image_player_up
        if self.falling:
            image = self.image_player_down
        if self.dead:
            image = self.image_player_dead
        # @ Todo : add a dead player image

        return image.convert_alpha()

    # Make the player jump (and fall)
    def player_jump(self):
        # Player is jumping.
        if self.jumping:
            self.color = 245, 35, 20
            self.rect.y -= 5
            # Player is now at max height !
            if self.rect.y <= 350:
                self.rect.y = 350
                self.jumping = False
                self.falling = True
        # Player is falling.
        if self.falling:
            self.color = 0, 0, 255
            self.rect.y += 5
            # Player is now at min height. (ground level)
            if self.rect.y >= 415:  # height - foot level.
                self.rect.y = self.foot_level - self.size_y
                self.jumping = False
                self.falling = False

        # To keep the code running.
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y

        self.image = self.get_player_image()

    def move_corpse(self):
        self.rect.x -= 6
        self.rect.y += 3

        # To keep the code running.
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y

    # Increments player score.
    def score_counter(self):
        if not self.dead:
            self.score += 1

        return self.score

    # If the player dies.
    def player_dies(self):
        self.dead = True
        self.image = self.image_player_dead.convert_alpha()
