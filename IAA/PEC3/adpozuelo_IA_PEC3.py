## Antonio Díaz Pozuelo - IA - PEC3 - adpozuelo@uoc.edu
## Python 3.6

import array
import itertools
from random import shuffle
from deap import creator, base, tools, algorithms

## Exercise 1
print()
# Assignature's reference codification
assignatures={'1':'CAT', '2': 'CAS', '3': 'ING', '4': 'MAT', '5': 'CIE', '6':'FYQ', '7': 'EFI', '8': 'VAL'}

# Create solution
def createSolution(pcls):
    S=[1,]*16+[2,]*16+[3,]*12+[4,]*16+[5,]*12+[6,]*12+[7,]*8+[8,]*8 # Assignatures vector solution
    shuffle(S) # Shuffle the solution
    part = pcls(S) # Create the individual's DEAP Object
    return part # return the solution

# Defining individuals
creator.create("FitnessMax", base.Fitness, weights=(1.0,)) # Individual's objective: maximize
creator.create("Individual", array.array, typecode="d", fitness=creator.FitnessMax) # Individual's structure (array)
toolbox = base.Toolbox()
toolbox.register("individual", createSolution, creator.Individual) # Individual's source
toolbox.register("population", tools.initRepeat, list, toolbox.individual) # Population source

## Exercise 2

# Objective function
def p(individual):
    hs=25; hd=5; # hs=hours/week, hd=hours/day
    Pg=0.0; Ph=0.0; Pv=0.0; # P() awards accumulators
    x=1; y=0.75; z=4.6875 # P() awards
    for j in range(len(individual)): # For each assignature   
        if j<hs: # Award 1, “no puede haber dos grupos haciendo la misma asignatura a la vez”
            a=[individual[j], individual[j+hs], individual[j+2*hs], individual[j+3*hs]] # Vector with column asignatures
            for e,q in itertools.combinations(a, 2): # Make combinations
                if e!=q: # If assignatures are different
                    Pg+=x # Emit award
        if j%hd==0: # Award 2, “cada grupo solo puede hacer como máximo una hora de una misma asignatura cada día”
            b=individual[j:j+hd] # Vector with 5 day's asignatures
            for e,q in itertools.combinations(b, 2): # Make combinations
                if e!=q: # If assignatures are different
                    Ph+=y # Emit award
        if j%hs==0: # Award 3, "respetar la tabla de horas semanales por asignatura y grupo"
            rep={} # Assignatures count histogram
            for t in range(hs): # Assignatures in 5 days, 25 hours
                if str(int(individual[j+t])) not in rep: # If assignature doesn't exist in histogram
                    rep[str(int(individual[j+t]))]=1 # Create and count 1
                else: # If it exist
                    rep[str(int(individual[j+t]))]+=1 # Add 1 to counter
            # If assignature in histogram respect restriction, emit award
            if '1' in rep and int(rep['1']) <= int(4): Pv+=z
            if '2' in rep and int(rep['2']) <= int(4): Pv+=z
            if '3' in rep and int(rep['3']) <= int(3): Pv+=z
            if '4' in rep and int(rep['4']) <= int(4): Pv+=z
            if '5' in rep and int(rep['5']) <= int(3): Pv+=z
            if '6' in rep and int(rep['6']) <= int(3): Pv+=z
            if '7' in rep and int(rep['7']) <= int(2): Pv+=z
            if '8' in rep and int(rep['8']) <= int(2): Pv+=z
    P=Pg+Ph+Pv # Add all awards to P
    return P, # Return objective function to maximize

## Exercise 3

pop=[10, 50, 100, 200, 400] # Population sizes for study
ngen=[100, 500, 1000, 2000, 4000] # Generation sizes for study

for pp in pop:
    toolbox.register("evaluate", p) # Register objective function
    toolbox.register("mate", tools.cxOnePoint) # Define the crossover function
    #toolbox.register("mate", tools.cxTwoPoint) # Define the crossover function
    #toolbox.register("mate", tools.cxUniform, indpb=0.1) # Define the crossover function
    toolbox.register("select", tools.selTournament, tournsize=3) # Define selection strategy
    #toolbox.register("select", tools.selBest, k=5) # Define selection strategy
    population = toolbox.population(n=pp) # Create population

    for g in ngen:
        bs=[]; Pmax=450; error=[]; ogen=0 # Best solution, P() maximum value and iteration counter
        for gen in range(g): # For each generation
            ogen=gen # Store the generation (iteration)
            offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.0) # Generate new population
            fits = toolbox.map(toolbox.evaluate, offspring) # Compute fitness values for the new population
            for fit, ind in zip(fits, offspring): # Associate new fitness with new individuals
                ind.fitness.values = fit
            population = toolbox.select(offspring, k=len(population)) # Replace old population with the new one
            top = tools.selBest(population, k=1) # Select the best solution
            error.append(Pmax-(p(top[0])[0])) # Calculate error for the best solution
            bs=[top[0], error[-1]] # Store the best solution and its error
            ## If method doesn't converge
            if len(error)>10 and error[-1]==error[-2]==error[-3]==error[-4]==error[-5]==error[-6]==error[-7]==error[-8]==error[-9]==error[-10]:
                break # Exit
    
            # Print configuration, iterations needed and best solution error.    
        print("generations = " + str(g)+ ", population = " + str(pp) + ", iterations = " + str(ogen) + ", error = "+ str(round(bs[1],6)))# + ", %error = " + str(round(bs[1]*100/Pmax,2))+"%")
# Print table with assignature's codes from best solution 
# for i in range(len(bs[0])):
#     if i!=0 and i%25==0:
#         print()
#     print(assignatures[str(int(bs[0][i]))] + " ", end='')
print()