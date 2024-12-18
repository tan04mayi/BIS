import numpy as np

def optimization_function(position):
    return position[0]*2 + position[1]*2

def initialize_parameters():
    grid_size = (10, 10)
    num_iterations = 100
    neighborhood_size = 1
    return grid_size, num_iterations, neighborhood_size

def initialize_population(grid_size):
    population = np.random.uniform(-10, 10, (grid_size[0], grid_size[1], 2))
    return population

def evaluate_fitness(population):
    fitness = np.zeros((population.shape[0], population.shape[1]))
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            fitness[i, j] = optimization_function(population[i, j])
    return fitness

def update_states(population, fitness, neighborhood_size):
    updated_population = np.copy(population)
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            x_min = max(i - neighborhood_size, 0)
            x_max = min(i + neighborhood_size + 1, population.shape[0])
            y_min = max(j - neighborhood_size, 0)
            y_max = min(j + neighborhood_size + 1, population.shape[1])
            best_neighbor = population[i, j]
            best_fitness = fitness[i, j]
            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    if fitness[x, y] < best_fitness:
                        best_neighbor = population[x, y]
                        best_fitness = fitness[x, y]
            updated_population[i, j] = (population[i, j] + best_neighbor) / 2
    return updated_population

def parallel_cellular_algorithm():
    grid_size, num_iterations, neighborhood_size = initialize_parameters()
    population = initialize_population(grid_size)
    best_solution = None
    best_fitness = float('inf')
    for iteration in range(num_iterations):
        fitness = evaluate_fitness(population)
        min_fitness = np.min(fitness)
        if min_fitness < best_fitness:
            best_fitness = min_fitness
            best_solution = population[np.unravel_index(np.argmin(fitness), fitness.shape)]
        population = update_states(population, fitness, neighborhood_size)
        print(f"Iteration {iteration + 1}: Best Fitness = {best_fitness}")
    print(f"Best Solution: {best_solution}, Best Fitness: {best_fitness}")
    return best_solution, best_fitness

if __name__ == "__main__":
    parallel_cellular_algorithm()
