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
        # Build 20 random synapses weights.
        default_synapses = self.default_synapses_weight()

        # You can paste the terminal output here to override the default_synapses of the bunnies.
        # default_synapses = [1.4, 0.6399999999999999, 0.24999999999999994, 1.88, 0.53, 0.3, 0.44999999999999996, -0.54, 0.68, -0.72, -0.8, 0.15999999999999998, -0.67, 1.4100000000000001, 0.24999999999999994, 0.36, 0.44000000000000006, 1.24, 1.08, 0.61]

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
    def breed(self, best_individual, stupidity_factor):

        # Get the brain pattern of the best individual.
        synapses = best_individual.synapses

        # Manually put him in the population.
        self.population.append(Individual(synapses))

        #  If the best individual from last population is stupid.
        if stupidity_factor > 10:
            synapses = self.default_synapses_weight()

        # Create the offsprings and make them mutate.
        for i in range(self.pop_size):
            newborn = Individual(synapses)

            # Send info about how many gens did not improve to the mutate function.
            newborn.mutate(stupidity_factor)
            self.population.append(newborn)

    # Build 20 random synapses weights.
    def default_synapses_weight(self):
        return [
            random.randint(-9, 9) / 100,
            random.randint(-9, 9) / 100,
            random.randint(-9, 9) / 100,
            random.randint(-9, 9) / 100,
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
