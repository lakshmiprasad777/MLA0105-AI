def is_valid_state(state):
    # Check if the state is valid (no missionaries eaten)
    left_bank = state[:3]
    right_bank = state[3:]
    return all(m <= c or m == 0 for m, c in zip(left_bank, right_bank))

def is_goal_state(state, goal):
    # Check if the state is the goal state
    return state == goal

def generate_successors(state, capacities):
    # Generate valid successor states
    successors = []

    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                successor = list(state)
                successor[i] -= 1
                successor[j] += 1

                if all(0 <= s <= c for s, c in zip(successor, capacities)) and is_valid_state(successor):
                    successors.append(tuple(successor))

    return successors

def dfs_search(initial_state, goal_state, capacities):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal_state(current_state, goal_state):
            return True

        successors = generate_successors(current_state, capacities)
        stack.extend(successors)

    return False

def get_user_input():
    try:
        capacities = list(map(int, input("Enter the capacities of the banks (format: M C): ").split()))
        initial_state = tuple(map(int, input("Enter the initial state (format: M C M C B): ").split()))
        goal_state = tuple(map(int, input("Enter the goal state (format: M C M C B): ").split()))

        if sum(capacities) == sum(initial_state) == sum(goal_state) and all(c >= 0 for c in capacities):
            return initial_state, goal_state, capacities
        else:
            print("Invalid input. Please ensure the total capacities and counts are consistent.")
            return get_user_input()
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()

if __name__ == "__main__":
    initial_state, goal_state, capacities = get_user_input()

    if dfs_search(initial_state, goal_state, capacities):
        print("Solution found!")
    else:
        print("No solution found.")
