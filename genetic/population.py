from genetic.individual import Individual
import random


# Holds individuals instances.
# Has a individual max number.
class Population:

    def __init__(self):
        self.pop_size = 16
        self.population = []
        self.best_individual = False

    # Create a default population of individuals.
    def create_default_pop(self):
        # Create the individuals

        # Build 20 random synapses weights.
        default_synapses = [
            random.randint(-1, 1) / 100,
            random.randint(-1, 1) / 100,
            random.randint(-1, 1) / 100,
            random.randint(-1, 1) / 100,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]


        # You can paste the terminal output here to override the default_synapses of the bunnies.
        # These synapses weights made the bunnies achieved a high score of 10886
        # default_synapses = [1.22, 0.030000000000000027, -0.21000000000000002, 1.0, 2.31, 0.010000000000000009, -0.1100000000000001, -1.1400000000000001, -0.97, 1.05, -0.98, 0.11000000000000004, -0.75, 1.25, 1.4100000000000001, -0.9299999999999999, -1.03, 0.33999999999999997, 1.11, -0.029999999999999916]

        for i in range(self.pop_size):
            self.population.append(Individual(default_synapses))

    # The individual who survived
    def get_best_individual(self, population):

        for individual in population:

            if not self.best_individual:
                self.best_individual = individual

            # If new challenger is better.
            if individual.score > self.best_individual.score:
                print('New best individual')
                print(individual.score)
                print(individual.synapses)
                self.best_individual = individual

        return self.best_individual

    # Breeding involves mutation.
    def breed(self, best_individual):

        synapses = best_individual.synapses

        # Manually put the best from last pop
        self.population.append(Individual(synapses))

        # Create the offsprings and make them mutate.
        for i in range(self.pop_size):
            newborn = Individual(synapses)
            newborn.mutate()
            self.population.append(newborn)
