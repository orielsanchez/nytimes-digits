import argparse
from operations_order import operations_order


def main():
    parser = argparse.ArgumentParser(description='Operations Order Tool')
    parser.add_argument('-n', '--numbers', nargs='+', type=int, required=True,
                        help='Input numbers separated by spaces')
    parser.add_argument('-t', '--target', type=int, required=True,
                        help='Target number')
    parser.add_argument('-s', '--solutions', type=int, default=10,
                        help='Number of solutions to display (default: 10)')
    args = parser.parse_args()

    numbers = args.numbers
    target = args.target
    num_solutions = args.solutions

    solutions = operations_order(numbers, target)

    print("Operations Order Tool")
    print("---------------------")
    print("Input Numbers:", numbers)
    print("Target:", target)
    print()

    if solutions:
        num_solutions = min(num_solutions, len(solutions))
        print(f"Showing {num_solutions} out of {len(solutions)} solutions:")
        for i, solution in enumerate(solutions[:num_solutions]):
            print(f"{i + 1}. {solution}")
    else:
        print("No solutions found.")


if __name__ == '__main__':
    main()
