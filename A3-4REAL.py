import copy




class BlockWorldAgent:
    def __init__(self):
        pass


    def solve(self):
        class State:
            def __init__(self, current_state, goal_state, total_num, moves=None):
                if moves is None:
                    moves = []
                self.current_state = current_state
                self.goal_state = goal_state
                self.total_num = total_num
                self.moves = moves


            def __eq__(self, other):
                return (self.current_state == other.current_state and
                        self.goal_state == other.goal_state and
                        self.total_num == other.total_num and
                        self.moves == other.moves)


            def __hash__(self):
                return hash((tuple(map(tuple, self.current_state)),
                             tuple(map(tuple, self.goal_state)),
                             self.total_num,
                             tuple(self.moves)))


            def goal_state_move(self, depth_limit):
                return self.iterative_deepening(depth_limit)


            def iterative_deepening(self, depth_limit):
                for limit in range(1, depth_limit + 1):
                    result, final_state = self.dls(limit)
                    if result is not None:
                        return result, final_state
                return None, None


            def dls(self, depth_limit):
                return self.recursive_dls(self, depth_limit)


            def recursive_dls(self, node, depth):
                if node.difference() == 0:
                    return node.moves, node.current_state
                elif depth == 0:
                    return None, None


                for index, stack in enumerate(node.current_state):
                    for index2, stack2 in enumerate(node.current_state):
                        if index != index2:
                            new_state = self.move_block(node, index, index2)
                            if new_state:
                                result, final_state = self.recursive_dls(new_state, depth - 1)
                                if result is not None:
                                    return result, final_state


                for index, stack in enumerate(node.current_state):
                    if len(stack) > 1:
                        new_state = self.move_block(node, index, -1)
                        if new_state:
                            result, final_state = self.recursive_dls(new_state, depth - 1)
                            if result is not None:
                                return result, final_state


                return None, None


            def move_block(self, state, from_stack, to_stack):
                temp_table = copy.deepcopy(state.current_state)
                if from_stack == to_stack:
                    return None
                if to_stack == -1:
                    to_stack = len(temp_table)
                if not temp_table[from_stack]:
                    return None
                block = temp_table[from_stack].pop()
                temp_table[to_stack].append(block)
                return State(temp_table, state.goal_state, state.total_num, state.moves + [(block, to_stack if to_stack != len(temp_table) else 'Table')])


            def difference(self):
                same_num = 0
                for left_stack, right_stack in zip(self.current_state, self.goal_state):
                    same_num += sum(1 for x, y in zip(left_stack, right_stack) if x == y)
                return self.total_num - same_num


        initial_arrangement = [["A"], ["C", "B"]]
        goal_arrangement = [[], ["C", "B", "A"]]
        total_num = sum(len(stack) for stack in initial_arrangement)


        # Fix: Provide arguments to the State constructor
        state = State(initial_arrangement, goal_arrangement, total_num)
        depth_limit = 10  # You can adjust the depth limit according to your requirements
        solution, final_state = state.goal_state_move(depth_limit)


        if solution is not None:
            print("Solution found:")
            print("Moves:", solution)
            print("Final State:")
            print(final_state)
        else:
            print("No solution found within the depth limit.")


        return solution, final_state


agent = BlockWorldAgent()
result = agent.solve()
print(result)
