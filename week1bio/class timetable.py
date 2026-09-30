Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import random

# -----------------------------------
# INPUT DATA
# -----------------------------------

classes = [
    {"subject": "Maths", "faculty": "F1", "group": "G1"},
    {"subject": "Physics", "faculty": "F2", "group": "G1"},
    {"subject": "C Programming", "faculty": "F3", "group": "G2"},
    {"subject": "DBMS", "faculty": "F4", "group": "G2"},
    {"subject": "OS", "faculty": "F5", "group": "G3"},
    {"subject": "Networks", "faculty": "F2", "group": "G3"}
]

rooms = ["R1", "R2", "R3"]

slots = [
    "9:00-10:00",
    "10:00-11:00",
    "11:00-12:00",
    "12:00-1:00"
]

# -----------------------------------
# PARAMETERS
# -----------------------------------

POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1


# -----------------------------------
# CREATE RANDOM CHROMOSOME
# -----------------------------------

def create_chromosome():
    chromosome = []

    for _ in classes:
        slot = random.choice(slots)
        room = random.choice(rooms)

        chromosome.append((slot, room))

    return chromosome


# -----------------------------------
# CREATE INITIAL POPULATION
# -----------------------------------

def create_population():
    return [
        create_chromosome()
        for _ in range(POPULATION_SIZE)
    ]


# -----------------------------------
# FITNESS FUNCTION
# -----------------------------------

def fitness(chromosome):

    clashes = 0

    # Compare every pair of classes
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):

            slot_i, room_i = chromosome[i]
            slot_j, room_j = chromosome[j]

            # Check only if classes occur
            # at the same time
            if slot_i == slot_j:

                # Room clash
                if room_i == room_j:
                    clashes += 1

                # Faculty clash
                if classes[i]["faculty"] == classes[j]["faculty"]:
                    clashes += 1

                # Student group clash
                if classes[i]["group"] == classes[j]["group"]:
                    clashes += 1

    return 1 / (1 + clashes)


# -----------------------------------
# SELECTION
# -----------------------------------

def selection(population):

    population.sort(
        key=fitness,
        reverse=True
    )

    # Select best half
    return population[:len(population) // 2]


# -----------------------------------
# SINGLE POINT CROSSOVER
# -----------------------------------

def crossover(parent1, parent2):

    point = random.randint(
        1,
        len(classes) - 1
    )

    child1 = (
        parent1[:point] +
        parent2[point:]
    )

    child2 = (
        parent2[:point] +
        parent1[point:]
    )

    return child1, child2


# -----------------------------------
# MUTATION
# -----------------------------------

def mutation(chromosome):

    for i in range(len(chromosome)):

        if random.random() < MUTATION_RATE:

            # Randomly change slot
            new_slot = random.choice(slots)

            # Randomly change room
            new_room = random.choice(rooms)

            chromosome[i] = (
                new_slot,
                new_room
            )

    return chromosome


# -----------------------------------
# GENETIC ALGORITHM
# -----------------------------------

def genetic_algorithm():

    population = create_population()

    for generation in range(GENERATIONS):

        # Check best chromosome
...         best = max(
...             population,
...             key=fitness
...         )
... 
...         # If no clashes
...         if fitness(best) == 1:
...             print("Solution found!")
...             return best
... 
...         # Selection
...         selected = selection(population)
... 
...         new_population = []
... 
...         # Elitism
...         new_population.append(selected[0])
... 
...         # Create new population
...         while len(new_population) < POPULATION_SIZE:
... 
...             parent1 = random.choice(selected)
...             parent2 = random.choice(selected)
... 
...             child1, child2 = crossover(
...                 parent1,
...                 parent2
...             )
... 
...             child1 = mutation(child1)
...             child2 = mutation(child2)
... 
...             new_population.append(child1)
... 
...             if len(new_population) < POPULATION_SIZE:
...                 new_population.append(child2)
... 
...         population = new_population
... 
...     # Return best solution after generations
...     return max(
...         population,
...         key=fitness
...     )
... 
... 
... # -----------------------------------
... # DISPLAY TIMETABLE
... # -----------------------------------
... 
... def display_timetable(solution):
... 
...     print("\n========== TIMETABLE ==========\n")
... 
...     for i, cls in enumerate(classes):
... 
...         slot, room = solution[i]
... 
...         print(
...             f"{cls['subject']:15}"
...             f"Faculty: {cls['faculty']:5}"
            f"Group: {cls['group']:5}"
            f"Slot: {slot:15}"
            f"Room: {room}"
        )

    print("\nFitness:", fitness(solution))

    if fitness(solution) == 1:
        print("Status: CLASH-FREE")
    else:
        print("Status: Clashes exist")


# -----------------------------------
# MAIN
# -----------------------------------

solution = genetic_algorithm()

