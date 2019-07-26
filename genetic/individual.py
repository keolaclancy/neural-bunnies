import math
import random
from src.player import Player


# Class that defines an individual of a generation.
# It must perform Jumping when needed
# We should be able to determine the fitness of an individual.
# We need to feed this class with a player instance.
class Individual(Player):

    # Set default attribute.
    def __init__(self, synapses):
        super().__init__(450)  # @todo : import display.height instead.

        # All the weights of the synapses
        self.synapses = synapses

    # Update synapses weights.
    # The more generations that can't beat high score, the more we mutate.
    def mutate(self, stupidity_factor):

        synapses = self.synapses

        self.synapses = []
        # For each weight, change it a little bit.
        # The best the fitness, the less the change
        for synapse in synapses:
            rand = random.randint(0, 100) + stupidity_factor * 2
            delta = rand / 100

            # If the bunnies are stuck doing stupid things, some should mutate more.
            if delta > 0.5:
                new_weight = synapse + delta
            elif delta > 0.9:
                new_weight = synapse + delta + 0.1
            elif delta < 0.2:
                new_weight = synapse - delta - 0.1
            else:
                new_weight = synapse - delta

            self.synapses.append(new_weight)

    # Sigmoid method.
    def sigmoid(self, x):

        x = x / 100
        return 1 / (1 + math.exp(-x))

    # This is the fitness based on the score the individual achieved.
    # Goes from 0 to 1.
    #  Probably not needed as we will keep the best anyway.
    def get_fitness(self):
        fitness = self.sigmoid(self.score)
        return fitness

    # Make dem bunnies jump (random for now)
    def do_jump(self):
        if not self.jumping:
            if not self.falling:
                self.jumping = True
