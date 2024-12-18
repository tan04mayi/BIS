import random

POPULATION_SIZE = 100

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "I love GeeksforGeeks"

class Individual:
    '''
    Class representing an individual in the population.
    '''
    def _init_(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @staticmethod
    def mutated_gene():
        '''
        Create a random gene for mutation.
        '''
        return random.choice(GENES)

    @staticmethod
    def create_gnome():
        '''
        Create a chromosome (list of genes) of the same length as the target string.
        '''
        return [Individual.mutated_gene() for _ in range(len(TARGET))]

    def mate(self, partner):
        '''
        Perform mating and produce a new offspring.
        '''
        child_chromosome = []
        for gene_self, gene_partner in zip(self.chromosome, partner.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gene_self)
            elif prob < 0.90:
                child_chromosome.append(gene_partner)
            else:
                child_chromosome.append(Individual.mutated_gene())
        return Individual(child_chromosome)

    def calculate_fitness(self):
        '''
        Calculate the fitness score as the number of differing characters.
        Lower fitness is better (0 is the optimal score).
        '''
        return sum(gene != target_gene for gene, target_gene in zip(self.chromosome, TARGET))

def main():
    generation = 1
    found = False
    population = [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

    while not found:
        # Sort the population by fitness (lower is better)
        population.sort(key=lambda individual: individual.fitness)

        # If the best individual has fitness 0, the target string is found
        if population[0].fitness == 0:
            found = True
            break

        # Create a new generation
        new_generation = []

        # Carry forward the top 10% of individuals
        top_individuals = int(0.1 * POPULATION_SIZE)
        new_generation.extend(population[:top_individuals])

        # Mating to fill the remaining 90% of the population
        remaining_population = POPULATION_SIZE - top_individuals
        for _ in range(remaining_population):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        # Print the best individual of the current generation
        best_individual = population[0]
        print(f"Generation: {generation}\tString: {''.join(best_individual.chromosome)}\tFitness: {best_individual.fitness}")

        generation += 1

    # Print the final generation and the best individual
    best_individual = population[0]
    print(f"Generation: {generation}\tString: {''.join(best_individual.chromosome)}\tFitness: {best_individual.fitness}")

if _name_ == "_main_":
    main()