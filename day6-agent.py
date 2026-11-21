import random

# Objective function: we want to maximize this function
def objective_function(x):
    return -(x - 5) ** 2 + 25


# Hill Climbing algorithm
def hill_climbing():
    current = random.uniform(-10, 10)
    step_size = 0.1

    print(f"Starting point: {current:.2f}")

    while True:
        left = current - step_size
        right = current + step_size

        # Evaluate neighboring solutions
        current_score = objective_function(current)
        left_score = objective_function(left)
        right_score = objective_function(right)

        # Move toward a better solution
        if left_score > current_score:
            current = left
        elif right_score > current_score:
            current = right
        else:
            break

    print("\nOptimization completed!")
    print(f"Best solution (x): {current:.2f}")
    print(f"Maximum value: {objective_function(current):.2f}")


if __name__ == "__main__":
    hill_climbing()
    