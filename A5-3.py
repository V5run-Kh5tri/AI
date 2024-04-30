import random
import math

def generate_formula(sol):
    a, b, c, d = sol
    clause1 = (not a) or d
    clause2 = c or b
    clause3 = (not c) or (not d)
    clause4 = (not d) or (not b)
    clause5 = (not a) or (not d)
    return sum([clause1, clause2, clause3, clause4, clause5])

def move(soln):
    new_sol = list(soln)
    flip_index = random.randint(0, 3)
    new_sol[flip_index] = 1 - new_sol[flip_index]
    new_sol = tuple(new_sol)
    return new_sol

def simulated_annealing(initial_sol, temp, cooling_func, num_iterations):
    current_sol = initial_sol
    current_val = generate_formula(current_sol)
    moves = [(current_sol, current_val)]
   
    for _ in range(num_iterations):
        new_sol = move(current_sol)
        new_val = generate_formula(new_sol)
        delta_e = new_val - current_val
       
        if delta_e > 0:
            current_sol = new_sol
            current_val = new_val
        else:
            probability = math.exp(delta_e / temp)
            if random.random() < probability:
                current_sol = new_sol
                current_val = new_val
               
        temp = cooling_func(temp)
        moves.append((current_sol, current_val))
       
        if temp <= 0:
            break  

    return moves

initial_solution = (1, 1, 1, 1)
initial_temperature = 500
cooling_function = lambda t: t - 50 if t > 50 else 1  
num_iterations = 10

sa_moves = simulated_annealing(initial_solution, initial_temperature, cooling_function, num_iterations)
for next_move in sa_moves:
    print(f"Solution: {next_move[0]}, Clause satisfied: {next_move[1]}")
