import pygame
import math

from genetic.population import Population
from src.obstacle_manager import ObstacleManager


# This is the main genetic handler.
class Genetic:

    def __init__(self, screen, size):
        # Display attributes
        self.screen = screen
        self.size = size

        self.font = pygame.font.Font('ressources/font/DroidSansMono.ttf', 20)
        self.font_small = pygame.font.Font('ressources/font/DroidSansMono.ttf', 12)

        # Genetic attributes
        self.training_enabled = False
        self.pop = Population()
        self.pool = []  # The population of individuals
        self.gen_number = 1  # The generation number
        self.best_score = 0  # The best score for an individual

    # Enable or disable the training.
    def toggle_training(self, enabled):
        if enabled:
            self.training_enabled = True
        else:
            self.training_enabled = False

    # Create a default population of stupid bunnies.
    def init(self):
        # Create a default population.
        self.pop.create_default_pop()
        self.pool = self.pop.population

    # Reset the pool
    def next_pop(self):
        # Get the last gen survivor
        best_individual = self.pop.get_best_individual(self.pool)

        # Reset the pool.
        self.pool = []
        self.gen_number += 1

        # Prepare next population.
        self.pop.breed(best_individual)
        self.pool = self.pop.population

    def gen_watcher(self):
        best_individual = self.pop.get_best_individual(self.pool)

        # Display population data
        self.display_gen_data(best_individual.score)
        # Display the neural network
        self.display_neural_network(best_individual)

    def think(self, player, display):
        # Get the inputs.
        inputs = self.get_inputs(player, display)

        # Feed the inputs to a function
        determined_output = self.determine_output(inputs, player)

        # print(determined_output)
        if determined_output > 0.5:
            self.output_jump(player)

    # From 0 to 1
    def determine_output(self, inputs, player):

        # The 4 inputs
        i1 = int(inputs[0])
        i2 = int(inputs[1])
        i3 = inputs[2]
        i4 = inputs[3]

        # Inputs to layer weights
        w_i1_j1 = player.synapses[0]
        w_i1_j2 = player.synapses[1]
        w_i1_j3 = player.synapses[2]
        w_i1_j4 = player.synapses[3]

        w_i2_j1 = player.synapses[2]
        w_i2_j2 = player.synapses[3]
        w_i2_j3 = player.synapses[4]
        w_i2_j4 = player.synapses[5]

        w_i3_j1 = player.synapses[4]
        w_i3_j2 = player.synapses[5]
        w_i3_j3 = player.synapses[6]
        w_i3_j4 = player.synapses[7]

        w_i4_j1 = player.synapses[6]
        w_i4_j2 = player.synapses[7]
        w_i4_j3 = player.synapses[8]
        w_i4_j4 = player.synapses[9]

        # Layer to output weights
        w_j1_k1 = player.synapses[10]
        w_j2_k1 = player.synapses[11]
        w_j3_k1 = player.synapses[12]
        w_j4_k1 = player.synapses[13]

        bias = 2
        j1 = player.sigmoid((i1 * w_i1_j1 + i2 * w_i2_j1 + i3 * w_i3_j1 + i4 * w_i4_j1) + bias)
        j2 = player.sigmoid((i1 * w_i1_j2 + i2 * w_i2_j2 + i3 * w_i3_j2 + i4 * w_i4_j2) + bias)
        j3 = player.sigmoid((i1 * w_i1_j3 + i2 * w_i2_j3 + i3 * w_i3_j3 + i4 * w_i4_j3) + bias)
        j4 = player.sigmoid((i1 * w_i1_j4 + i2 * w_i2_j4 + i3 * w_i3_j4 + i4 * w_i4_j4) + bias)

        k1 = j1 * w_j1_k1 + j2 * w_j2_k1 + j3 * w_j3_k1 + j4 * w_j4_k1
        #
        # k1 = k1 / 10

        return player.sigmoid(k1)

    #  player status, obstacle distances.
    def get_inputs(self, player, display):

        obstacles = display.om.get_obstacles()
        obstacle_positions = self.get_obstacle_positions(obstacles)

        # We need to know the distance from the first obstacle
        if len(obstacle_positions) > 0:
            next_obstacle_dist = obstacle_positions[0] - (player.pos_x + player.size_x)
        else:
            next_obstacle_dist = 1

        # We need to know how far is the next obstacle
        if len(obstacle_positions) > 1:
            obstacle_spacing = obstacle_positions[1] - obstacle_positions[0]
        else:
            obstacle_spacing = 1

        jump_fall = 0
        # obstacle_spacing = 0
        # if player.jumping:
        #     if player.falling:
        #         jump_fall = 1

        inputs = [
            jump_fall,  # If player is already jumping
            player.pos_y,
            next_obstacle_dist,  # The distance between the player and next obstacle
            obstacle_spacing,  # The spacing between 1st and 2nd obstacle
        ]

        return inputs

    # Get the x coords of obstacles.
    def get_obstacle_positions(self, obstacles):
        obstacles_pos = []

        for obstacle in obstacles:
            obstacles_pos.append(obstacle.pos_x)

        return obstacles_pos

    # Make the bunny jump.
    def output_jump(self, individual):
        individual.do_jump()

    # Use the om from display to reset obstacles.
    def reset_obstacles(self, display):
        display.om.clear_all_obstacles()

    def display_gen_data(self, player_score):
        color = 255, 171, 0

        #  Display alive individuals.
        gen_string = 'Bunnies alive : {:05d}'.format(len(self.pool))
        text = self.font.render(gen_string, True, color)
        text_rect = text.get_rect()
        text_rect.top = 20
        text_rect.right = self.size[0] - 20
        self.screen.blit(text, text_rect)

        #  Display current gen.
        gen_string = 'Generation : {:05d}'.format(self.gen_number)
        text = self.font.render(gen_string, True, color)
        text_rect = text.get_rect()
        text_rect.top = 40
        text_rect.right = self.size[0] - 20
        self.screen.blit(text, text_rect)

        #  Display the best score an individual could achieve.
        if player_score > self.best_score:
            self.best_score = player_score

        gen_string = 'Best Score : {:05d}'.format(self.best_score)
        text = self.font.render(gen_string, True, color)
        text_rect = text.get_rect()
        text_rect.top = 60
        text_rect.right = self.size[0] - 20
        self.screen.blit(text, text_rect)

    # Display the neural network of an individual. (the best in this case)
    def display_neural_network(self, player):
        green = 0, 170, 0
        white = 255, 255, 255
        black = 0, 0, 0
        red = 255, 0, 0
        orange = 230, 82, 0

        i1_pos = (30, 30)
        i2_pos = (30, 70)
        i3_pos = (30, 110)
        i4_pos = (30, 150)

        j1_pos = (120, 30)
        j2_pos = (120, 70)
        j3_pos = (120, 110)
        j4_pos = (120, 150)

        k1_pos = (160, 90)

        circles = [
            i1_pos,  # I1
            i2_pos,  # I2
            i3_pos,  # I3
            i4_pos,  # I4

            j1_pos,  # J1
            j2_pos,  # J2
            j3_pos,  # J3
            j4_pos,  # J4

            k1_pos,  # K1
        ]

        # Draw circles
        for circle in circles:
            pygame.draw.circle(self.screen, (255, 255, 255), circle, 8, 1)

        # Build lines data
        lines = []
        for synapse in player.synapses:
            if synapse > 2:
                color = white
            elif synapse > 0:
                color = green
            elif synapse > -1:
                color = orange
            elif synapse > -2:
                color = red
            else:
                color = black

            lines.append(color)

        lines_coord = [

            # Lines from i1
            [i1_pos, j1_pos],  # w_i1_j1
            [i1_pos, j2_pos],  # w_i1_j2
            [i1_pos, j3_pos],  # w_i1_j3
            [i1_pos, j4_pos],  # w_i1_j4

            # Lines from i2
            [i2_pos, j1_pos],  # w_i2_j1
            [i2_pos, j2_pos],  # w_i2_j2
            [i2_pos, j3_pos],  # w_i2_j3
            [i2_pos, j4_pos],  # w_i2_j4

            # Lines from i3
            [i3_pos, j1_pos],  # w_i3_j1
            [i3_pos, j2_pos],  # w_i3_j2
            [i3_pos, j3_pos],  # w_i3_j3
            [i3_pos, j4_pos],  # w_i3_j4

            # Lines from i4
            [i4_pos, j1_pos],  # w_i4_j1
            [i4_pos, j2_pos],  # w_i4_j2
            [i4_pos, j3_pos],  # w_i4_j3
            [i4_pos, j4_pos],  # w_i4_j4

            # Lines from J layer to K
            [j1_pos, k1_pos],  # w_j1_k1
            [j2_pos, k1_pos],  # w_j2_k1
            [j3_pos, k1_pos],  # w_j3_k1
            [j4_pos, k1_pos],  # w_j4_k1
        ]

        # Draw lines
        i = 0
        for line in lines:
            pygame.draw.line(self.screen, line, lines_coord[i][0], lines_coord[i][1], 2)
            i += 1
