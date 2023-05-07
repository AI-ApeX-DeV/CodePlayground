import random

def fitness(individual):
    """Calculates the fitness of an individual"""
    return sum([1 for c in individual if c == '1'])

def generate_individual(length):
    """Generates a random individual"""
    return ''.join([random.choice(['0', '1']) for _ in range(length)])

def mutate(individual, mutation_rate):
    """Mutates an individual with the given mutation rate"""
    mutated = ''
    for c in individual:
        if random.random() < mutation_rate:
            mutated += '1' if c == '0' else '0'
        else:
            mutated += c
    return mutated

def genetic_algorithm(population_size, num_generations, mutation_rate, chromosome_length, strings):
    # Generate initial population
    population = [generate_individual(chromosome_length) for _ in range(population_size)]
    
    # Evolution loop
    for generation in range(num_generations):
        # Evaluate fitness of each individual
        fitness_scores = [fitness(individual) for individual in population]
        
        # Select parents
        parent1 = random.choices(population, weights=fitness_scores)[0]
        parent2 = random.choices(population, weights=fitness_scores)[0]
        
        # Crossover parents to create offspring
        midpoint = random.randint(0, len(parent1) - 1)
        child = parent1[:midpoint] + parent2[midpoint:]
        
        # Mutate offspring
        child = mutate(child, mutation_rate)
        
        # Replace random individual in population with offspring
        population[random.randint(0, len(population) - 1)] = child
        
    # Return individual with highest fitness
    return max(population, key=fitness)

# Example usage
strings = ['1001', '1100', '1101']
individual = genetic_algorithm(population_size=100, num_generations=1000, mutation_rate=0.1, chromosome_length=len(strings[0]), strings=strings)
print(individual)
