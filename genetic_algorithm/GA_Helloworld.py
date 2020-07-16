import random


class Population:
    def __init__(self, p, m, num):
        self.popSize = num
        self.generation = 0
        self.finished = False
        self.target = p
        self.mutationRate = m
        self.best = ''
        self.population = firstPopulation(self.popSize, len(target))
        self.fitness = list()
        self.matingPool = list()
        self.bestIndex = -1

    def calcFitness(self):
        for p in self.population:
            fitness = 0
            for i in range(len(self.target)):
                if p[i] == self.target[i]:
                    fitness += 1
            self.fitness.append(fitness)

    def naturalSelection(self):
        maxFitness = 0
        index = -1
        for f in self.fitness:
            if maxFitness <= self.fitness[f]:
                maxFitness = self.fitness[f]
                index = f
        if maxFitness == len(self.target):
            self.finished = True
        self.best = self.population[index]
        self.matingPool = []
        for i, p in enumerate(self.fitness):
            # putting the same DNA in the mating pool p**2 times to increase its probability being chosen
            for t in range(p**2):
                self.matingPool.append(self.population[i])
        self.fitness = []

    def childGeneretion(self):
        parent1 = self.matingPool[random.randint(0, len(self.matingPool) - 1)]
        parent2 = self.matingPool[random.randint(0, len(self.matingPool) - 1)]
        division = random.randint(0, len(self.target) - 1)
        child = list()
        for gene in range(len(parent1)):
            if gene < division:
                child.append(parent1[gene])
            else:
                child.append(parent2[gene])
        for i in range(len(child)):
            if random.uniform(0, 1) <= self.mutationRate:
                child[i] = charGenerate()

        return child

    def newPopulation(self):
        self.population = []
        for p in range(self.popSize):
            self.population.append(self.childGeneretion())
        self.generation += 1


# generating a random character
def charGenerate():
    c = random.randint(63, 122)
    if c == 63:     # For space
        c = 32
    if c == 64:     # For full stop (.)
        c = 46

    return chr(c)


def firstPopulation(num, targetSize):
    pop = list()
    dna = list()
    for n in range(num):
        for i in range(targetSize):
            dna.append(charGenerate())
        pop.append(dna)
        dna = []
    return pop


def getBest(lst):
    txt = ''
    for l in lst:
        txt += l

    return txt


target = 'Hello world'
populationSize = 200
mutationRate = 0.01
# initialize the population with random DNA
population = Population(target, mutationRate, populationSize)

while not population.finished:
    # calculate fitness
    population.calcFitness()
    # create the mating pool
    population.naturalSelection()
    # generate a child
    population.childGeneretion()
    # create a new population with the generated child
    population.newPopulation()
    # get the best DNA
    best = getBest(population.best)

    print(f'best : {best} | generation {population.generation}')
