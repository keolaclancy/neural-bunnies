from src.obstacle import Obstacle
import pygame
import random


# Manage how obstacles should appear and disappear
class ObstacleManager:

    def __init__(self, ground_height, width):
        self.width = width
        self.foot_level = ground_height
        self.screen_width = width
        self.obstacles = []  # Array of obstacle instances.
        self.minimum_spacing = 50  # The minimum space between 2 obstacles.

    # Create obstacle instance and put it in the array.
    def create_obstacle(self):
        if len(self.obstacles) < 3:

            # If there is no obstacles.
            # @todo : Ugly code to refacto
            if len(self.obstacles) == 1:
                if self.obstacles[0].pos_x < (self.width - self.minimum_spacing):
                    obstacle = Obstacle(self.foot_level, self.width + random.randint(0, 150))
                    self.obstacles.append(obstacle)
            if len(self.obstacles) == 2:
                if self.obstacles[1].pos_x < (self.width - self.minimum_spacing):
                    obstacle = Obstacle(self.foot_level, self.width + random.randint(0, 50))
                    self.obstacles.append(obstacle)
            if len(self.obstacles) == 0:
                obstacle = Obstacle(self.foot_level, self.width + random.randint(0, 200))
                self.obstacles.append(obstacle)

    # Return an array of obstacles instances.
    def get_obstacles(self):
        return self.obstacles

    # Clear all obstacles.
    def clear_all_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.pos_x = - 50

    # Remove an obstacle instance.
    def remove_obstacle(self):
        for obstacle in self.obstacles:
            if obstacle.pos_x < 0:
                self.obstacles.remove(obstacle)
                del obstacle

    # Make the obstacle move.
    def move_obstacle(self):
        for obstacle in self.obstacles:
            obstacle.pos_x -= obstacle.speed

    # Check if the player rect collides with an obstacle.
    def check_collision(self, player):
        player_rect = pygame.Rect(0, 0, player.size_x, player.size_y)  # The rect.
        player_rect.x = player.pos_x
        player_rect.y = player.pos_y

        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(0, 0, obstacle.size_y, obstacle.size_x)
            obstacle_rect.x = obstacle.pos_x
            obstacle_rect.y = obstacle.pos_y

            # Player dies when colliding.
            if pygame.Rect.colliderect(player_rect, obstacle_rect):
                player.player_dies()

    # Run the manager.
    def run(self):
        self.create_obstacle()
        self.move_obstacle()
        self.remove_obstacle()

        return self.get_obstacles()

