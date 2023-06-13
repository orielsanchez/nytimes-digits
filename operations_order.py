def operations_order(numbers, target):
    operators = ['+', '-', '*', '/']
    solutions = set()  # Use a set to store unique solutions

    def dfs(expr, curr_result, remaining_numbers, used_numbers):
        if curr_result == target:
            solutions.add(tuple(expr))  # Convert the expression to a tuple to make it hashable

        if len(remaining_numbers) == 0 or curr_result == target:
            return

        for i, num in enumerate(remaining_numbers):
            next_remaining = remaining_numbers[:i] + remaining_numbers[i + 1:]
            next_used = used_numbers + [num]
            for op in operators:
                if op == '/':
                    if num == 0 or (curr_result is not None and curr_result % num != 0):
                        continue  # Skip division by zero or non-integer division
                if curr_result is None:
                    dfs([num], num, next_remaining, next_used)
                else:
                    new_result = calculate(curr_result, op, num)
                    if new_result is not None and new_result >= 0:
                        dfs(expr + [op, num], new_result, next_remaining, next_used)

    def calculate(curr_result, operator, operand):
        if operator == '+':
            return curr_result + operand
        elif operator == '-':
            return curr_result - operand
        elif operator == '*':
            return curr_result * operand
        elif operator == '/':
            return curr_result // operand if curr_result % operand == 0 else None

    dfs([], None, numbers, [])

    if solutions:
        solutions = list(solutions)  # Convert the set back to a list
        solutions.sort(key=len)  # Sort solutions by the smallest number of elements to the largest
        solutions = solutions[:3]  # Limit solutions to the first 10
        return solutions
    else:
        return None


# Test cases
test_cases = [
    ([1, 2, 3, 4, 5, 10], 65),
    ([2, 7, 9, 10, 15, 25], 167),
    ([3,4,5,9,11,20], 248),
    ([5,7,11,15,20,22], 335),
    ([4,7,14,15,20,24], 482),
    ([1,2,3,4,5], 999)
]

for numbers, target in test_cases:
    solutions = operations_order(numbers, target)
    if solutions:
        print("Numbers:", numbers)
        print("Target:", target)
        print("Solutions:")
        for solution in solutions:
            print("Order of operations:", solution)
        print()
    else:
        print("Numbers:", numbers)
        print("Target:", target)
        print("No solution found.")
        print()
