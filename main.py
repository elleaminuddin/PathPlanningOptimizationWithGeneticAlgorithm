#!/usr/bin/env python

from numpy import average
from numpy.core.fromnumeric import mean
from tools.population import population
from tools.fitness import fitness
from tools.ranking import ranking
from tools.dna import dna
from tools.draw_plot import show_plot
from tools.evolution import evolution_plot
from tools.ave import average_plot

from config import Config

def main():
    """
    encapsulates the capabilty of initializing chromosome population
    and then continue calculating fitness, generate ranking, perform crossover and
    mutation & repeating above steps until a defined stopping criteria is not met.
    """

    "Calls on the population function"
    chr_population = population()

    "Calls on the fitness function"
    chr_pop_fitness, chr_best_fitness_index = fitness(chr_pop=chr_population)

    "Calls on the rank function to generate ranking"
    chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness, pop=chr_population)

    "Calls on the crossover and mutation function"
    chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
        ranked_population=chr_ranked_population, chr_best_fitness_index=
        chr_best_fitness_index, last_pop=chr_population)

    show_plot(best_chromosome=chr_crossover_mutated_population[0])

    while not Config.stop_generation:

        prev_best_fit = chr_pop_fitness[chr_best_fitness_index[0], 0]

        chr_pop_fitness, chr_best_fitness_index = fitness(
            chr_pop=chr_crossover_mutated_population)

        chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness, 
            pop=chr_crossover_mutated_population)

        chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
            ranked_population=chr_ranked_population, chr_best_fitness_index=
            chr_best_fitness_index, last_pop=chr_crossover_mutated_population)
        
        print("Best chromosome is:", chr_crossover_mutated_population[chr_best_fitness_index[0]]) 
        
        if prev_best_fit == chr_pop_fitness[chr_best_fitness_index[0], 0]:
            Config.stop_criteria += 1
        else:
            Config.stop_criteria = 0

        if Config.stop_criteria >= 5:
            Config.stop_generation = True

        show_plot(best_chromosome=chr_crossover_mutated_population[0])
        progress = []
        for i in range(0, Config.generations+1):
            progress.append(sum(chr_crossover_mutated_population[chr_best_fitness_index[i]]))
        ave = []
        for i in range(0, Config.generations+1):
            ave.append(mean(chr_pop_fitness[i]))

        Config.generations += 1

    show_plot(best_chromosome=chr_crossover_mutated_population[0], inf_time=True)
    evolution_plot(progress)
    average_plot(ave)

if __name__ == '__main__':

    main()
